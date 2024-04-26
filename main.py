from ultralytics import YOLO

model = YOLO("yolov8n")

# Detect objects from classes 0 and 1 only
classes = [0]

# Set the confidence threshold
conf_thresh = 0.5

# Set the source of the input data (e.g., image file, video file, or folder containing images)
source = "input_videos/securitycam.mp4"

# Call the predict function with the specified parameters
results = model.predict("input_videos/securitycam.mp4", save=True, classes=classes, conf=conf_thresh)