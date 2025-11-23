# Virtual Calculator Web App

A modern, AI-powered virtual calculator that allows you to perform calculations using hand gestures via your webcam.

## Features

-   **AI Hand Tracking**: Powered by MediaPipe for robust, lighting-invariant hand detection.
-   **Web Interface**: Built with FastAPI and Vanilla JS for a smooth browser experience.
-   **Touchless Interaction**:
    -   **Point**: Use your **Index Finger** to move the cursor.
    -   **Click**: **Pinch** (Index Finger + Thumb) to press buttons.

## Prerequisites

-   Python 3.8+
-   Webcam

## Quick Start (Recommended)

**macOS / Linux**:
```bash
./run.sh
```

**Windows**:
Double-click `run.bat` or run in terminal:
```cmd
run.bat
```

## Manual Installation

If you prefer to set it up manually:

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd Virtual-Calculator
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Start the application**:
    ```bash
    uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
    ```

2.  **Open in Browser**:
    Navigate to [http://localhost:8000](http://localhost:8000).

3.  **Grant Permissions**:
    Allow the browser to access your camera when prompted.

## Project Structure

```
Virtual-Calculator/
├── backend/            # Python backend (FastAPI)
│   ├── main.py        # Server entry point & WebSocket logic
│   └── utils.py       # Calculator drawing & logic
├── static/             # Frontend assets
│   ├── index.html     # Web interface
│   ├── style.css      # Styling
│   └── script.js      # Client-side logic
├── data/               # Configuration
│   └── values.txt     # Calculator layout coordinates
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Technologies

-   **Backend**: FastAPI, OpenCV, MediaPipe, NumPy
-   **Frontend**: HTML5, CSS3, JavaScript (WebSocket)
