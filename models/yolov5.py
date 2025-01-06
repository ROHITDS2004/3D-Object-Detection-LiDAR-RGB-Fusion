import torch
from torchvision.models.detection import yolov5

class YOLOv5:
    def __init__(self):
        self.model = yolov5(pretrained=True)

    def __call__(self, image):
        # Perform object detection
        return self.model(image)