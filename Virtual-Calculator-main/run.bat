@echo off

REM Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install it first.
    pause
    exit /b
)

REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
call .venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run the application
echo Starting Virtual Calculator...
echo Open http://localhost:8000 in your browser
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

pause
