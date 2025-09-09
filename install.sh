#!/bin/bash

# Household Resource Optimization Agent - Installation Script
# This script sets up the virtual environment and installs all dependencies

set -e  # Exit on any error

echo "🏠 Household Resource Optimization Agent - Installation"
echo "======================================================"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or higher is required. Found: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION found"

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ -d "household_agent_env" ]; then
    echo "⚠️  Virtual environment already exists. Removing old one..."
    rm -rf household_agent_env
fi

python3 -m venv household_agent_env

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source household_agent_env/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create database directory if it doesn't exist
mkdir -p household_agent

# Make run script executable
chmod +x household_agent/run.sh

echo ""
echo "🎉 Installation completed successfully!"
echo ""
echo "To start the application:"
echo "1. Activate the virtual environment:"
echo "   source household_agent_env/bin/activate"
echo ""
echo "2. Start the application:"
echo "   cd household_agent"
echo "   ./run.sh"
echo ""
echo "   Or start manually:"
echo "   uvicorn app:app --reload --port 8000 &"
echo "   streamlit run frontend.py --server.port 8501"
echo ""
echo "3. Access the application:"
echo "   Frontend: http://localhost:8501"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "Happy optimizing! 🚀"
