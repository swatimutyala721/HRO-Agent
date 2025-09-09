# Household Resource Optimization Agent (HRO-Agent)

A smart household management system that helps optimize resource usage, track inventory, and provide consumption insights using machine learning predictions.

## Features

- **Inventory Management**: Track food items, energy usage, and water consumption
- **Consumption Logging**: Record daily usage patterns
- **Smart Predictions**: ML-powered forecasting for next week's resource needs
- **Optimization Suggestions**: AI-driven recommendations for reducing waste and costs
- **Real-time Dashboard**: Interactive web interface for easy management

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit
- **Database**: SQLite with SQLAlchemy ORM
- **ML/Analytics**: scikit-learn, pandas, numpy
- **Data Validation**: Pydantic

## Project Structure

```
HRO-Agent/
├── household_agent/
│   ├── app.py              # FastAPI backend
│   ├── frontend.py         # Streamlit frontend
│   ├── models.py           # SQLAlchemy database models
│   ├── schemas.py          # Pydantic data schemas
│   ├── crud.py             # Database operations & ML predictions
│   ├── database.py         # Database configuration
│   └── run.sh              # Startup script
├── household_agent_env/    # Virtual environment
├── .gitignore
└── README.md
```

## Installation

### Quick Install (Recommended)

**For macOS/Linux:**
```bash
git clone <repository-url>
cd HRO-Agent
chmod +x install.sh
./install.sh
```

**For Windows:**
```bash
git clone <repository-url>
cd HRO-Agent
install.bat
```

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd HRO-Agent
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv household_agent_env
   source household_agent_env/bin/activate  # On Windows: household_agent_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start

1. **Start the application**
   ```bash
   cd household_agent
   chmod +x run.sh
   ./run.sh
   ```

   Or start services manually:
   ```bash
   # Terminal 1: Start FastAPI backend
   cd household_agent
   source ../household_agent_env/bin/activate
   uvicorn app:app --reload --port 8000

   # Terminal 2: Start Streamlit frontend
   cd household_agent
   source ../household_agent_env/bin/activate
   streamlit run frontend.py --server.port 8501
   ```

2. **Access the application**
   - **Frontend**: http://localhost:8501
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs

### Features Overview

#### Inventory Management
- Add items with name, quantity, unit, category, and expiration date
- Filter inventory by category (food, energy, water)
- View current stock levels

#### Consumption Tracking
- Log daily consumption of resources
- Track usage patterns over time
- Automatic inventory updates when items are consumed

#### Smart Analytics
- **Usage Prediction**: ML models predict next week's resource needs
- **Waste Reduction**: Alerts for items approaching expiration
- **Cost Optimization**: Suggestions for energy and water savings
- **Eco Tips**: Recommendations for sustainable living

## API Endpoints

- `POST /items/` - Add new inventory item
- `GET /items/` - Get inventory items (with optional category filter)
- `POST /logs/` - Log resource consumption
- `GET /suggestions/` - Get optimization recommendations

## Database Schema

### Inventory Items
- `id`: Primary key
- `name`: Item name
- `quantity`: Current quantity
- `unit`: Measurement unit (kg, liters, etc.)
- `category`: Item category (food, energy, water)
- `expiration_date`: Expiration date for perishables

### Consumption Logs
- `id`: Primary key
- `item_id`: Reference to inventory item
- `quantity`: Amount consumed
- `timestamp`: When consumption occurred
- `resource_type`: Type of resource consumed

## Machine Learning Features

The system uses linear regression to predict future resource consumption based on historical data:

- **Food Usage Prediction**: Forecasts weekly food consumption
- **Energy Forecasting**: Predicts energy usage patterns
- **Water Usage Analysis**: Estimates water consumption trends

## Development

### Adding New Features

1. **Database Changes**: Update `models.py` and run migrations
2. **API Endpoints**: Add routes in `app.py`
3. **Frontend**: Modify `frontend.py` for UI changes
4. **Business Logic**: Update `crud.py` for new operations

### Testing

```bash
# Test API endpoints
curl http://localhost:8000/items/
curl http://localhost:8000/suggestions/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- [ ] Integration with smart home devices
- [ ] Mobile app development
- [ ] Advanced ML models for better predictions
- [ ] Integration with grocery delivery APIs
- [ ] Energy usage monitoring with IoT sensors
- [ ] Cost tracking and budget management
- [ ] Social features for household collaboration

## Support

For issues and questions, please open an issue in the GitHub repository.