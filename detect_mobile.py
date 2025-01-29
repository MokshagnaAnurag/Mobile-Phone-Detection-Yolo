import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model (Make sure you have the correct weights path)
model = YOLO("yolo-Weights/yolov8n.pt")

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set frame width
cap.set(4, 480)  # Set frame height

# Define class names (currently just 'cell phone')
classNames = ["cell phone"]

while True:
    # Capture frame from webcam
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture frame.")
        break

    # Resize image for better performance
    img = cv2.resize(img, (640, 480))

    try:
        # Perform object detection using YOLO
        results = model(img, stream=True)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]  # Extract bounding box coordinates
                conf = box.conf[0]  # Confidence score
                cls = int(box.cls[0])  # Class ID

                # Check if the detected class is "cell phone" and confidence is above threshold
                if classNames[cls] == "cell phone" and conf > 0.5:
                    # Draw bounding box and label on image
                    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(img, f"{classNames[cls]}: {conf:.2f}", (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    except Exception as e:
        # Error handling for inference
        print(f"Error during inference: {e}")

    # Display the output image with detection results
    cv2.imshow("Mobile Phone Detection", img)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
