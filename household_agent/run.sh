#!/bin/bash
# Run Household Agent

# Activate virtual environment
source household_agent_env/bin/activate

# Start FastAPI backend in background
cd household_agent
uvicorn app:app --reload --port 8000 &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start Streamlit frontend
streamlit run frontend.py --server.port 8501

# Cleanup: kill backend when frontend exits
kill $BACKEND_PID