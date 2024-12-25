import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolo-Weights/yolov8n.pt")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

classNames = ["cell phone"]

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture frame.")
        break

    img = cv2.resize(img, (640, 480))

    try:
        results = model(img, stream=True)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = box.conf[0]
                cls = int(box.cls[0])

                if classNames[cls] == "cell phone" and conf > 0.5:
                    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(img, f"{classNames[cls]}: {conf:.2f}", (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    except Exception as e:
        print(f"Error during inference: {e}")

    cv2.imshow("Mobile Phone Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()