const video = document.getElementById('videoElement');
const canvas = document.getElementById('outputCanvas');
const ctx = canvas.getContext('2d');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const statusDiv = document.getElementById('status');

let stream = null;
let ws = null;
let intervalId = null;

// Set canvas size to match backend processing size
canvas.width = 800;
canvas.height = 600;

startButton.addEventListener('click', startCamera);
stopButton.addEventListener('click', stopCamera);

async function startCamera() {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;

        startButton.disabled = true;
        stopButton.disabled = false;

        connectWebSocket();
    } catch (err) {
        console.error("Error accessing camera:", err);
        statusDiv.textContent = "Status: Error accessing camera";
    }
}

function stopCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
    }

    if (ws) {
        ws.close();
        ws = null;
    }

    if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
    }

    startButton.disabled = false;
    stopButton.disabled = true;
    statusDiv.textContent = "Status: Disconnected";

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function connectWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `${protocol}//${window.location.host}/ws`;

    ws = new WebSocket(wsUrl);

    ws.onopen = () => {
        statusDiv.textContent = "Status: Connected";
        startSendingFrames();
    };

    ws.onmessage = (event) => {
        const img = new Image();
        img.onload = () => {
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        };
        img.src = "data:image/jpeg;base64," + event.data;
    };

    ws.onclose = () => {
        statusDiv.textContent = "Status: Disconnected";
        stopCamera();
    };

    ws.onerror = (error) => {
        console.error("WebSocket error:", error);
        statusDiv.textContent = "Status: WebSocket Error";
    };
}

function startSendingFrames() {
    const fps = 30;
    intervalId = setInterval(() => {
        if (ws && ws.readyState === WebSocket.OPEN && video.readyState === video.HAVE_ENOUGH_DATA) {
            // Draw video frame to a temporary canvas to get data URL
            const tempCanvas = document.createElement('canvas');
            tempCanvas.width = video.videoWidth;
            tempCanvas.height = video.videoHeight;
            const tempCtx = tempCanvas.getContext('2d');

            // Mirror the video locally if needed, but backend does flipping too
            // Let's send raw frame
            tempCtx.drawImage(video, 0, 0);

            const dataUrl = tempCanvas.toDataURL('image/jpeg', 0.8);
            ws.send(dataUrl);
        }
    }, 1000 / fps);
}
