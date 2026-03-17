from webcam_detector import webcam_detection
from gemini_client import explain_scene
import cv2
import time



def main():
    cap = cv2.VideoCapture(0)
    last_explain = 0
    interval = 30
    last_scene = set()  # simpan scene terakhir yang dijelaskan

    while True:
    # Titik 1
        try:
            frame, scene_objects, annotated_frame = webcam_detection(cap)
        except Exception as e:
            print(f"Webcam error: {e}")
            break

        if frame is None:
            break

        cv2.imshow("Webcam Detection", annotated_frame)
        if scene_objects:
            current_scene = set(scene_objects)
            scene_changed = current_scene != last_scene
        # Titik 2
            if scene_changed and time.time() - last_explain > interval:
                try:
                    explanation = explain_scene(scene_objects)
                    print("\nAI Explanation:", explanation)
                    last_explain = time.time()
                    last_scene = current_scene  # update scene terakhir
                except Exception as e:
                    print(f"Gemini error: {e}")
                    # tidak break — program tetap jalan meski Gemini gagal

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()