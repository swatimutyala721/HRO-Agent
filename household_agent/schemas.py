# Data Schemas

### Define Pydantic models for data validation and serialization.

import time
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InventoryItemBase(BaseModel):
    name: str
    quantity: float
    unit: str
    category: str
    expiration_date: datetime

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItem(InventoryItemBase):
    id: int
    
    class Config:
        from_attributes = True

class ConsumptionLogBase(BaseModel):
    item_id: int
    quantity: float
    resource_type: str

class ConsumptionLogCreate(ConsumptionLogBase):
    pass

class ConsumptionLog(ConsumptionLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
