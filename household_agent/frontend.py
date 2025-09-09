# Streamlit Frontend for Household Agent

### run with streamlit run frontend.py. It interacts with the backend at localhost:8000

import streamlit as st
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000"

st.title("Household Resource Optimization Agent")

# Add Inventory Item
st.header("Add Item to Inventory")
name = st.text_input("Name")
quantity = st.number_input("Quantity", min_value=0.0)
unit = st.text_input("Unit (e.g., kg)")
expiration = st.date_input("Expiration Date")
category = st.selectbox("Category", ["food", "energy", "water"])

if st.button("Add Item"):
    data = {
        "name": name,
        "quantity": quantity,
        "unit": unit,
        "expiration_date": datetime.combine(expiration, datetime.min.time()).isoformat(),
        "category": category
    }
    response = requests.post(f"{BASE_URL}/items/", json=data)
    if response.status_code == 200:
        st.success("Item added!")

# Log Consumption
st.header("Log Consumption")
item_id = st.number_input("Item ID", min_value=1)
amount = st.number_input("Amount Consumed", min_value=0.0)
resource_type = st.selectbox("Resource Type", ["food", "energy", "water"])

if st.button("Log Consumption"):
    data = {"item_id": item_id, "quantity": amount, "resource_type": resource_type}
    response = requests.post(f"{BASE_URL}/logs/", json=data)
    if response.status_code == 200:
        st.success("Consumption logged!")

# View Inventory
st.header("Current Inventory")
category_filter = st.selectbox("Filter by Category", [None, "food", "energy", "water"])
params = {"category": category_filter} if category_filter else {}
response = requests.get(f"{BASE_URL}/items/", params=params)
if response.status_code == 200:
    items = response.json()
    st.table(items)

# Get Suggestions
st.header("Optimization Suggestions")
if st.button("Generate Suggestions"):
    response = requests.get(f"{BASE_URL}/suggestions/")
    if response.status_code == 200:
        suggestions = response.json()["suggestions"]
        for sug in suggestions:
            st.write(f"- {sug}")