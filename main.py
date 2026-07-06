import cv2
from ultralytics import YOLO
from ultralytics.solutions import speed_estimation

# Load the YOLOv8n model
model = YOLO('yolov8n.pt')

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Create a box for speed estimation
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define the box for speed estimation
line_points = [(0, h // 2), (w, h // 2)] # (0, 240)----------(540, 240)

# Initialize the speed estimation object
speed_obj = speed_estimation.SpeedEstimator(
    region = line_points,
    show = False,
    fps = 30,
    line_width = 2
)

# Main loop to read frames from the webcam
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame from webcam. Exiting...")
        break

    frame = cv2.flip(frame, 1) # Flip the frame horizontally for a mirror effect

    # Perform object detection on the frame
    trsack = model.track(frame, persist=True, show=False, imgsz=320)

    # Draw the line for speed estimation
    speed_obj(frame)

    # Display the resulting frame
    cv2.imshow('Python Automation - Speed Detector', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()