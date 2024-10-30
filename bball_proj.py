import cv2
from inference_sdk import InferenceHTTPClient
from roboflow import Roboflow
from deep_sort_realtime.deepsort_tracker import DeepSort

rf = Roboflow(api_key="jMmuJYNVkmmxwOtwxfET")

project = rf.workspace("scu-ai-ball").project("scu-ball-ai")
version = project.version(4)
dataset = version.download("yolov8")
model = version.model

tracker = DeepSort(tracker=30, n_init=3, nn_budget=20)

def detect(frame):
	result = yolo.model(frame)
	detections = []

	for detection in results.pred[0]:
        x1, y1, x2, y2, conf, class_id = detection[:6]
        detections.append([x1, y1, x2, y2, conf])
    
    # Update DeepSORT with detections
    tracker_outputs = tracker.update(np.array(detections), frame)
    
    return tracker_outputs 







   