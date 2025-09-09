# Database Models for Household Agent

### We'll store inventory items (food), consumption logs, and basic resource usage (energy/water mocked as daily logs).

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from database import Base
from datetime import datetime

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Float)
    unit = Column(String) # grams, liters, etc.
    category = Column(String) # food, cleaning, etc.
    expiration_date = Column(DateTime)
    
class ConsumptionLog(Base):
    __tablename__ = "consumption_logs"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("inventory.id"))
    quantity = Column(Float)
    timestamp = Column(DateTime, default=datetime.now)
    resource_type = Column(String) # energy, water, etc.

    