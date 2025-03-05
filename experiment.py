import cv2
from ultralytics import YOLO

# Load YOLO model on CPU
model = YOLO("yolov8s.pt").to("cpu")  # Ensure model runs on CPU

# Open webcam (0 for built-in camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame, imgsz=320)  # Reduce size for faster processing

    # Draw bounding boxes on the frame
    annotated_frame = results[0].plot()

    # Display frame
    cv2.imshow("Real-Time Detection", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


