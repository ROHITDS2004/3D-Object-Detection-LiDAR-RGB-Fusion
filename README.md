# 3D Object Detection & Localization using LiDAR and RGB Fusion

Welcome to the **3D Object Detection & Localization** project, where we combine **LiDAR** and **RGB camera** data to create an advanced, real-time 3D object detection system. This system uses **PointNet++** to process LiDAR data, **YOLOv5** for object detection from RGB images, and **ROS** for seamless real-time deployment.

---

## Key Features
- **LiDAR Data Processing**: Efficiently handles 3D point clouds using **PointNet++**.
- **RGB Image Processing**: Detects objects in RGB images using the powerful **YOLOv5** model.
- **Sensor Fusion**: Merges LiDAR and RGB data to improve accuracy and enhance 3D object localization.
- **ROS Integration**: Integrates the system with **Robot Operating System (ROS)** for real-time applications in robotics.

---

## Installation

Ready to get started? Follow these steps to set up the project on your machine:

### 1. Clone the Repository
First, get the project code by cloning the repository:
```bash
git clone https://github.com/ROHITDS2004/3D-Object-Detection-LiDAR-RGB-Fusion.git
cd 3D-Object-Detection-LiDAR-RGB-Fusion
```

### 2. Install Dependencies
Once you've cloned the repository, install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up ROS
To ensure everything works smoothly with ROS, run the setup script:
```bash
bash scripts/setup_ros.sh
```

---

## Usage

Now that you're all set up, here's how you can train and test the model:

### Training the Model
To train the model using your own dataset, run:
```bash
python src/train.py
```

### Running Inference
To run inference (make predictions) on sample or real-world data, execute:
```bash
python src/inference.py
```

---

## Data Directory Overview

The `data/` folder is where all your data lives—whether it's for testing, training, or demonstration. Here's what you'll find:

### Files in `data/`
1. **`sample_lidar_data.pcd`**  
   - A sample **LiDAR** point cloud file in `.pcd` format. This contains 3D data from a LiDAR sensor and is used for the LiDAR processing pipeline.

2. **`sample_rgb_image.jpg`**  
   - A sample **RGB** image file in `.jpg` format. This is the 2D visual data from a camera, used for the image processing pipeline.

---

### Purpose of the Data Files
- **Testing & Demonstration**: You can use these files to test the system without needing real-world data.
- **Development**: They help during debugging and building out the pipelines for LiDAR and RGB data.
- **Documentation**: These files show what format your data should be in when you use the system.

---

### Where to Get More Data

You can use publicly available datasets or generate your own data. Here’s where you can find more:

#### 1. LiDAR Data (`.pcd`)
- Download LiDAR `.pcd` files from these sources:
  - [KITTI Dataset](https://www.cvlibs.net/datasets/kitti/)
  - [SemanticKITTI Dataset](http://www.semantic-kitti.org/dataset.html)
- Alternatively, generate synthetic data using **CARLA**: [CARLA Simulator](https://carla.org/)
- Example `.pcd` file: [bunny.pcd](https://github.com/PointCloudLibrary/pcl/blob/master/test/bunny.pcd)

#### 2. RGB Images (`.jpg`)
- Use your own camera images or download sample data from:
  - [COCO Dataset](https://cocodataset.org/#home)
  - [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)
- Example `.jpg` file: [lena.jpg](https://github.com/opencv/opencv/blob/master/samples/data/lena.jpg)

---

### Adding Your Own Data
Here’s how you can add your data to the project:

1. **Download or Generate Data**:
   - Grab a `.pcd` file for LiDAR data and a `.jpg` file for RGB data from the sources above.
   - You can also use tools like **Open3D** or **PCL** to create synthetic LiDAR data.

2. **Place Files in the `data/` Folder**:
   - Drop your `.pcd` and `.jpg` files into the `data/` folder.

3. **Update File Paths in Your Code**:
   - In scripts like `inference.py`, make sure the file paths point to your new data:
     ```python
     lidar_data = load_lidar_data("data/sample_lidar_data.pcd")
     rgb_data = load_rgb_image("data/sample_rgb_image.jpg")
     ```

---

### Example Workflow

Here’s a simple step-by-step guide to test the system:

1. **Download Sample Data**:
   - Grab a `.pcd` file (e.g., `bunny.pcd`) and a `.jpg` file (e.g., `lena.jpg`).
   - Save them in the `data/` folder.

2. **Run Inference**:
   - To run inference (make predictions with the model), execute:
     ```bash
     python src/inference.py
     ```
   - The script will load the sample data, process it, and give you the results.

---

### Example Data Files

Here are some links to sample data files you can use for testing:
- **LiDAR Data**: [bunny.pcd](https://github.com/PointCloudLibrary/pcl/blob/master/test/bunny.pcd)
- **RGB Image**: [lena.jpg](https://github.com/opencv/opencv/blob/master/samples/data/lena.jpg)

---

### Folder Structure After Adding Data

Here’s what the project structure will look like after you add your data:

```
3D-Object-Detection-LiDAR-RGB-Fusion/
│
├── data/
│   ├── bunny.pcd  # Sample LiDAR data
│   └── lena.jpg   # Sample RGB image
│
├── src/           # Source code for training and inference
├── scripts/       # Setup and utility scripts
├── requirements.txt  # Python dependencies
└── README.md      # Project documentation
```

---

## Contributing

Want to contribute? We’d love your help! Here’s how you can get involved:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is open-source and licensed under the **MIT License**. Check out the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

Special thanks to these amazing tools and frameworks:
- **PointNet++**: For processing LiDAR point clouds with high precision.
- **YOLOv5**: For fast and accurate object detection in RGB images.
- **ROS**: For real-time robotic integration.

---

## Contact

If you have any questions or suggestions, feel free to reach out to me!

**Rohit DS**  
Email: rohitds2004@example.com  
GitHub: [ROHITDS2004](https://github.com/ROHITDS2004)  

---

Thank you for using the **3D Object Detection & Localization using LiDAR and RGB Fusion** project! 🚀
```
---