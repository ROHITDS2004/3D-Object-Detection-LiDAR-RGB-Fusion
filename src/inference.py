from lidar_processing import load_lidar_data, process_lidar_data
from rgb_processing import load_rgb_image, process_rgb_image
from fusion import fuse_data

def inference():
    """Run inference on LiDAR and RGB data."""
    lidar_data = load_lidar_data("data/sample_lidar_data.pcd")
    rgb_data = load_rgb_image("data/sample_rgb_image.jpg")
    
    lidar_features = process_lidar_data(lidar_data)
    rgb_detections = process_rgb_image(rgb_data)
    
    fused_data = fuse_data(lidar_features, rgb_detections)
    print("Fused Data:", fused_data)
    