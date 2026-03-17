import streamlit as st
import cv2
import time
from webcam_detector import webcam_detection  # pastikan fungsi ini mengembalikan frame, scene_objects, annotated_frame
from gemini_client import explain_scene  # pastikan fungsi ini menerima list objek dan mengembalikan penjelasan string

# Layout judul dan kolom
st.title("AI Vision Assistant")
col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("Live Webcam Feed")
    frame_placeholder = st.empty()

with col_right:
    st.subheader("🔍 Detected:")
    objects_placeholder = st.empty()

    st.subheader("🤖 AI Says:")
    explanation_placeholder = st.empty()

# Inisialisasi variabel
cap = cv2.VideoCapture(0)
last_explain_time = 0
interval = 5  # detik
last_scene = []
explanation = "Waiting for scene analysis..."

# Loop utama
while True:
    try:
        frame, scene_objects, annotated_frame = webcam_detection(cap)
    except Exception as e:
        st.error(f"Webcam error: {e}")
        break

    if frame is None:
        break

    # Tambahkan teks ke annotated_frame
    y_offset = 30
    for obj in scene_objects:
        cv2.putText(
            annotated_frame,
            f"Detected: {obj}",
            (20, y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )
        y_offset += 30
    short_explanation = explanation[:80] + "..." if len(explanation) > 80 else explanation
    cv2.putText(
        annotated_frame,
        explanation,
        (20, y_offset + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        1,
        cv2.LINE_AA
    )

    # Tampilkan frame ke Streamlit
    frame_placeholder.image(annotated_frame, channels="BGR")

    # Update objek terdeteksi
    if scene_objects:
        objects_placeholder.write("\n".join([f"• {obj}" for obj in scene_objects]))
    else:
        objects_placeholder.write("No objects detected")

    # Logic scene change + interval
    current_scene = tuple(scene_objects)
    scene_changed = current_scene != tuple(last_scene)

    if scene_changed and time.time() - last_explain_time > interval:
        try:
            explanation = explain_scene(scene_objects)
            last_explain_time = time.time()
            last_scene = scene_objects
        except Exception as e:
            explanation = f"Gemini error: {e}"

    explanation_placeholder.write(explanation)