import numpy as np
import open3d as o3d
from models.pointnet2 import PointNet2

def load_lidar_data(file_path):
    """Load LiDAR point cloud data."""
    pcd = o3d.io.read_point_cloud(file_path)
    points = np.asarray(pcd.points)
    return points

def process_lidar_data(points):
    """Process LiDAR data using PointNet++."""
    model = PointNet2()
    features = model(points)
    return features