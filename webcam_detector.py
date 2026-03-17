from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

def webcam_detection(cap, threshold=0.5):
    ret, frame = cap.read()
    if not ret:
        return None, None, None

    results = model(frame, conf=threshold)
    annotated_frame = results[0].plot()

    detections = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        if conf >= threshold:
            detections.append({
                "label": label,
                "confidence": round(conf * 100, 2),
                "bbox": [int(x1), int(y1), int(x2), int(y2)]
            })

    labels = [d["label"] for d in detections]
    scene_objects = list(set(labels))

    return frame, scene_objects, annotated_frame
