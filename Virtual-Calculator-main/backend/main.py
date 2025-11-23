from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import cv2
import numpy as np
import base64
import sys
import os
import mediapipe as mp
import math

# Add parent directory to path to import addon_function
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from . import utils as my

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

class CalculatorState:
    def __init__(self):
        self.ans = ""
        self.ab = ""
        self.a = -1
        self.b = -1
        self.clicked = False # To prevent multiple clicks per pinch
        
        # Load values once
        try:
            self.values = np.loadtxt('data/values.txt', int)
            self.x = self.values[0]
            self.y = self.values[1]
            self.h = self.values[2]
            self.w = self.values[3]
        except Exception as e:
            print(f"Error loading values: {e}")
            self.x, self.y, self.h, self.w = 100, 100, 50, 50

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    state = CalculatorState()
    
    try:
        while True:
            # Receive frame from client (base64 encoded)
            data = await websocket.receive_text()
            
            # Decode base64 image
            img_bytes = base64.b64decode(data.split(',')[1])
            nparr = np.frombuffer(img_bytes, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if frame is None:
                continue

            # Flip frame (mirror effect)
            frame = cv2.flip(frame, 1)
            
            # Resize for processing (keep logic consistent with index.py)
            frame = cv2.resize(frame, (800, 600))
            
            # Convert to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            # TO PRODUCE EFECT IF ANY KEY PRESSED
            if len(state.ab):
                state.a = int(state.ab[0])
                state.b = int(state.ab[1])
                clr = (0, 190, 0)
                
                if state.a == 0 and state.b == 5:
                    cv2.rectangle(frame, (state.x + state.w * state.a, state.y + state.h * (2 + state.b)), (state.x + state.w * (state.a + 2), state.y + state.h * (3 + state.b)), clr, -1)
                elif state.a == 3 and state.b == 2:
                    cv2.rectangle(frame, (state.x + state.w * state.a, state.y + state.h * (2 + state.b)), (state.x + state.w * (state.a + 1), state.y + state.h * (4 + state.b)), clr, -1)
                elif state.a == 3 and state.b == 4:
                    cv2.rectangle(frame, (state.x + state.w * state.a, state.y + state.h * (2 + state.b)), (state.x + state.w * (state.a + 1), state.y + state.h * (4 + state.b)), clr, -1)
                else:
                    cv2.rectangle(frame, (state.x + state.w * state.a, state.y + state.h * (2 + state.b)), (state.x + state.w * (state.a + 1), state.y + state.h * (3 + state.b)), clr, -1)

                state.ab = ""

            # DRAW CALC
            frame = my.draw_calc(frame, 15, -10)

            # Process Hands
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    
                    # Get coordinates
                    h, w, c = frame.shape
                    
                    # Index Finger Tip (Landmark 8)
                    index_tip = hand_landmarks.landmark[8]
                    ix, iy = int(index_tip.x * w), int(index_tip.y * h)
                    
                    # Thumb Tip (Landmark 4)
                    thumb_tip = hand_landmarks.landmark[4]
                    tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
                    
                    # Draw Pointer
                    cv2.circle(frame, (ix, iy), 10, (255, 0, 255), -1)
                    
                    # Calculate distance for click (Pinch)
                    distance = math.hypot(ix - tx, iy - ty)
                    
                    # Threshold for click (adjust as needed)
                    click_threshold = 60
                    
                    if distance < click_threshold:
                        cv2.circle(frame, (ix, iy), 10, (0, 255, 0), -1) # Green when clicked
                        
                        if not state.clicked:
                            # Perform Click Action
                            state.ans, state.ab = my.press_key(state.ans, ix, iy)
                            state.clicked = True
                    else:
                        state.clicked = False

            # MAKE ANSWER LONG ENOUGH TO DISPLAY ON DISPLAY BOARD
            l = len(state.ans)
            if l > 10:
                ans1 = state.ans[l - 9:l]
                ans1 = "..." + ans1
            else:
                ans1 = state.ans

            # WRITE ON DISPLAY BOARD
            cv2.putText(frame, ans1, (state.x + int(state.w * 0.15), state.y + int(state.h * 0.7)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Encode frame back to base64
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            
            await websocket.send_text(jpg_as_text)

    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close()
