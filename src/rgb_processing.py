import cv2
import torch
from models.yolov5 import YOLOv5

def load_rgb_image(file_path):
    """Load RGB image."""
    image = cv2.imread(file_path)
    return image

def process_rgb_image(image):
    """Process RGB image using YOLOv5."""
    model = YOLOv5()
    detections = model(image)
    return detections