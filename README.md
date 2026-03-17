# AI Vision Assistant

AI Vision Assistant is a real-time scene analysis application that combines YOLOv8 object detection with Google Gemini AI to analyze and describe what is happening in front of your webcam.

## Features
* Real-time object detection using YOLOv8
* AI-powered scene explanation using Google Gemini
* Smart scene change detection — Gemini is only called when the scene changes
* Live web interface built with Streamlit
* AI explanation overlay directly on the video feed

## Tech Stack
* Python
* YOLOv8 (Ultralytics) — real-time object detection
* Google Gemini API — AI scene explanation
* OpenCV — webcam capture and frame processing
* Streamlit — web interface

## Prerequisites
* Python 3.9+
* A webcam
* [Google Gemini API key](https://aistudio.google.com) — free tier available, no credit card required

## Installation
Clone the repository:
```
git clone https://github.com/einzeinn/ai-vision-assistant.git
cd ai-vision-assistant
```

Create a virtual environment:
```
python -m venv venv
```

Activate the virtual environment.

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Running the Application
```
streamlit run ui.py
```

## How It Works
1. The webcam captures frames in real-time
2. YOLOv8 detects objects in each frame and draws bounding boxes
3. Detected objects are compared to the previous scene
4. If the scene has changed, Google Gemini is called to generate an explanation
5. The explanation is displayed both on the video feed and in the sidebar

## Demo
![Demo Screenshot](demo.png)

## Future Improvements
* Add conversation memory so Gemini remembers previous scenes
* Support for multiple camera sources
* Export session summary to file
```

---

Dua hal yang perlu kamu lakukan setelah ini:

1. **Tambahkan screenshot demo** — ambil screenshot program saat jalan, simpan sebagai `demo.png` di root project, lalu push ke GitHub
2. **Push README ini** — simpan sebagai `README.md` di root project lalu:
```
git add .
git commit -m "Add README"
git push
