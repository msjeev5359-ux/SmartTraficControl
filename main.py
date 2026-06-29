import cv2
from ultralytics import YOLO
from traffic_logic import get_signal_timing

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("videos/road1.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls in [2, 5, 7]:  # car, bus, truck
                count += 1

    green_time = get_signal_timing(count)

    cv2.putText(frame, f"Vehicles: {count}", (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Green Time: {green_time}s", (50,100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Traffic System", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()