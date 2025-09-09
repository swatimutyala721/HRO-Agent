@echo off
REM Household Resource Optimization Agent - Installation Script (Windows)
REM This script sets up the virtual environment and installs all dependencies

echo 🏠 Household Resource Optimization Agent - Installation
echo ======================================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment
echo 📦 Creating virtual environment...
if exist "household_agent_env" (
    echo ⚠️  Virtual environment already exists. Removing old one...
    rmdir /s /q household_agent_env
)

python -m venv household_agent_env

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call household_agent_env\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create database directory if it doesn't exist
if not exist "household_agent" mkdir household_agent

echo.
echo 🎉 Installation completed successfully!
echo.
echo To start the application:
echo 1. Activate the virtual environment:
echo    household_agent_env\Scripts\activate.bat
echo.
echo 2. Start the application:
echo    cd household_agent
echo    uvicorn app:app --reload --port 8000
echo    streamlit run frontend.py --server.port 8501
echo.
echo 3. Access the application:
echo    Frontend: http://localhost:8501
echo    Backend API: http://localhost:8000
echo    API Docs: http://localhost:8000/docs
echo.
echo Happy optimizing! 🚀
pause
