# 📱 Mobile Phone Detection Using OpenCV and YOLO

![PYTHON](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![NUMPY](https://img.shields.io/badge/NUMPY-013243?style=for-the-badge&logo=numpy&logoColor=white) 
![OPENCV](https://img.shields.io/badge/OPENCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=none&logoColor=white)

This project demonstrates a **Mobile Phone Detection System** using OpenCV and the YOLOv3 (You Only Look Once) object detection algorithm. The program leverages a webcam for live footage and identifies mobile phones in real time, making it efficient and lightweight.

---

## 🎯 Features

- **Real-Time Detection**: Detects mobile phones with high accuracy using YOLOv3.
- **Optimized for Speed**: Ensures real-time performance for live webcam footage.
- **Clear Visual Feedback**: Highlights detected mobile phones with bounding boxes and confidence scores.
- **Ease of Use**: Minimal configuration required to get started.

---
## 🛠 Installation

### 1. Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### 2. Clone the Repository
```bash
git clone https://github.com/MokshagnaAnurag/Mobile-Phone-Detection-Yolo.git
cd Mobile-Phone-Detection-Yolo
```

### 3. Install Dependencies
Install the required Python libraries:
```bash
pip install opencv-python opencv-python-headless numpy
```

---

## ⚙️ YOLO Configuration Files

This project uses YOLOv3 for object detection. Ensure the following files are present in the project directory:

1. **`yolov3.weights`** - Pre-trained weights for YOLOv3.
2. **`yolov3.cfg`** - YOLOv3 configuration file.
3. **`coco.names`** - COCO dataset class labels.

### 🔗 Download Required Files
- [YOLOv3 Weights](https://pjreddie.com/media/files/yolov3.weights)
- [YOLOv3 Config](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- [COCO Class Names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

📂 **Ensure all three files are placed in the project directory.**

---

## 🚀 Usage

1. **Run the Script**:
   ```bash
   python detect_mobile.py
   ```

2. **Live Detection**:
   - The webcam will start, displaying a live feed.
   - Detected mobile phones will be highlighted with bounding boxes labeled `cell phone` and a confidence score.

3. **Exit**:
   - Press `q` to quit the live feed.

---

## 🗂 File Structure
```
mobile-phone-detection/
├── coco.names          # Class labels used by YOLO
├── detect_mobile.py    # Main Python script
├── yolov3.cfg          # YOLO configuration file
├── yolov3.weights      # YOLO pre-trained weights
└── README.md           # Documentation
```

## ❓ Troubleshooting

### Common Issues

1. **Gray or Blank Screen**:
   - Ensure no other application is using the webcam.
   - Verify the correct webcam index in the code:
     ```python
     cap = cv2.VideoCapture(0)  # Change '0' if using an external camera.
     ```
   - Test your webcam using the Camera app or another program.

2. **YOLO Configuration File Not Found**:
   - Ensure the `yolov3.weights`, `yolov3.cfg`, and `coco.names` files are in the project directory.

3. **Slow Performance**:
   - Use a smaller input blob size for faster detection (e.g., replace `(416, 416)` with `(320, 320)` in the code).

4. **Unable to Detect Objects**:
   - Check the class IDs in the `coco.names` file to confirm the correct label (`cell phone`).

---

## 🏗 Contributing

Contributions are welcome! If you'd like to add features or fix bugs, feel free to:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Submit a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- **[YOLO](https://pjreddie.com/darknet/yolo/)** by Joseph Redmon for the object detection algorithm.
- **[OpenCV](https://opencv.org/)** for the computer vision tools.
---
