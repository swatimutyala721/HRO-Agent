# FastAPI Backend for Household Agent

### run with uvicorn app:app --reload

from fastapi import FastAPI, Depends 
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from schemas import InventoryItemCreate, InventoryItem, ConsumptionLogCreate, ConsumptionLog
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/items/", response_model=InventoryItem)
def create_inventory_item(item: InventoryItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/", response_model=list[InventoryItem])
def read_items(category: str = None, db: Session = Depends(get_db)):
    return crud.get_items(db, category)

@app.post("/logs/", response_model=ConsumptionLog)
def create_log(log: ConsumptionLogCreate, db: Session = Depends(get_db)):
    return crud.log_consumption(db, log)

@app.get("/suggestions/")
def get_suggestions(db: Session = Depends(get_db)):
    return {"suggestions": crud.get_suggestions(db)}
