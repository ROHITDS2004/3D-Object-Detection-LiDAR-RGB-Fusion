import numpy as np

def fuse_data(lidar_features, rgb_detections):
    """Fuse LiDAR and RGB data using late fusion."""
    # Example: Concatenate features
    fused_features = np.concatenate((lidar_features, rgb_detections), axis=1)
    return fused_features