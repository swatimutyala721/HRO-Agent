#CRUD Operations

### Implement CRUD operations for inventory items and consumption logs.

from sqlalchemy.orm import Session
from models import InventoryItem, ConsumptionLog
from schemas import InventoryItemCreate, ConsumptionLogCreate
from datetime import datetime, timedelta
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import grocery_scraper

def create_item(db: Session, item: InventoryItemCreate):
    db_item = InventoryItem(
        **item.model_dump()
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, category: str = None):
    query = db.query(InventoryItem)
    if category:
        query = query.filter(InventoryItem.category == category)
    return query.all()

def log_consumption(db: Session, log: ConsumptionLogCreate):
    db_log = ConsumptionLog(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    # update inventory item quantity
    item = db.query(InventoryItem).filter(InventoryItem.id == log.item_id).first()
    if item:
        item.quantity -= log.quantity
        db.commit()
        db.refresh(item)
    return db_log

def get_logs(db: Session, resource_type: str = None):
    query = db.query(ConsumptionLog)
    if resource_type:
        query = query.filter(ConsumptionLog.resource_type == resource_type)
    return query.all()


# Prediction: Simple ML to predict next week's usage based on logs
def predict_usage(db: Session, resource_type: str):
    logs = get_logs(db, resource_type)
    if not logs:
        return "No data available"

    df = pd.DataFrame([log.__dict__ for log in logs])
    df['day'] = df['timestamp'].dt.dayofyear
    X = df[['day']].values
    y = df[['quantity']].values

    model = LinearRegression()
    model.fit(X, y)
    
    future_days = np.array([[df['day'].max() + i] for i in range(1, 8)])
    future_predictions = model.predict(future_days)
    return sum(future_predictions) # Total predicted for next week

# Suggestions: Basic Logic
def get_suggestions(db: Session):
    items = get_items(db)
    perishables = [item for item in items if item.category == 'food' and item.expiration_date < datetime.now() + timedelta(days=3)]

    suggestions = []
    if perishables:
        suggestions.append(f"Use these soon: {', '.join([item.name for item in perishables])}. Suggested meal: Salad with {perishables[0].name}.")
    
    food_pred = predict_usage(db, 'food')
    if isinstance(food_pred, float) and food_pred > 0:
        suggestions.append(f"Predicted food usage next week: {food_pred:.2f} units. Stock up if low.")
    
    # Grocery suggestions for low inventory items
    low_inventory_items = [item for item in items if item.quantity < 5]
    
    if low_inventory_items:
        suggestions.append("🛒 **Local Store Price Check:**")
        
        for item in low_inventory_items[:3]:  # Check top 3 low inventory items
            try:
                # Scrape from stores with timeout
                walmart_prices = grocery_scraper.get_walmart_prices(item.name)
                target_prices = grocery_scraper.get_target_prices(item.name)
                safeway_prices = grocery_scraper.get_safeway_prices(item.name)

                all_prices = walmart_prices + target_prices + safeway_prices
                if all_prices:
                    # Find cheapest price
                    valid_prices = [p for p in all_prices if p['price'] != 'N/A' and '$' in p['price']]
                    if valid_prices:
                        cheapest = min(valid_prices, key=lambda p: float(p['price'].replace('$', '').replace('Now ', '').replace(',', '')))
                        suggestions.append(f"• {item.name}: Cheapest at {cheapest['name']} - {cheapest['price']} {cheapest['discount']}")
                    else:
                        suggestions.append(f"• {item.name}: Check local stores for current prices")
                else:
                    # Fallback to general store suggestions
                    suggestions.append(f"• {item.name}: Check Walmart, Target, Safeway for deals")
            except Exception as e:
                # Fallback suggestions when scraping fails
                suggestions.append(f"• {item.name}: Check local stores - Walmart, Target, Safeway")
                suggestions.append(f"• Look for {item.name} in weekly ads and store apps")
    
    # Always add general local store suggestions
    suggestions.append("🛒 **Local Store Tips:**")
    suggestions.append("• Check Walmart, Target, and Safeway for weekly deals")
    suggestions.append("• Consider bulk buying for non-perishables to save money")
    suggestions.append("• Look for store brands to reduce costs by 20-30%")
    suggestions.append("• Download store apps for digital coupons and exclusive deals")
    suggestions.append("• Check local farmers markets for fresh produce discounts")

    # Mock energy/water suggestions
    energy_pred = predict_usage(db, 'energy')
    if isinstance(energy_pred, float):
        suggestions.append(f"Predicted energy usage: {energy_pred:.2f} kWh. Tip: Adjust thermostat to save 10%.")
    
    # Eco/cost tips (hardcoded; replace with crawled data later)
    suggestions.append("Eco tip: Buy discounted veggies from local markets to reduce waste.")
    
    return suggestions