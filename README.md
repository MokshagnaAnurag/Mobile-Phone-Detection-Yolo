```markdown
# Mobile Phone Detection Using OpenCV and YOLO

This project implements a **Mobile Phone Detection System** using OpenCV and the YOLO (You Only Look Once) object detection algorithm. It uses a webcam to provide live footage and identifies mobile phones in real-time.

## Features

- Real-time object detection using a webcam.
- Only detects mobile phones with high accuracy using the YOLOv3 model.
- Displays bounding boxes and confidence scores around detected mobile phones.
- Lightweight and optimized for efficient processing.

---

## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Clone the Repository
```bash
https://github.com/MokshagnaAnurag/Mobile-Phone-Detection-Yolo.git
cd Mobile-Phone-Detection-Yolo
```

### Install Dependencies
Install the required Python libraries:
```bash
pip install opencv-python opencv-python-headless numpy
```

---

## YOLO Configuration Files
This project uses YOLOv3 for object detection. Ensure you have the following files in the repository directory:

1. **`yolov3.weights`** - Pre-trained weights file for YOLOv3.
2. **`yolov3.cfg`** - Configuration file for YOLOv3.
3. **`coco.names`** - List of class labels used by YOLO.

### Download Files
- Download the YOLOv3 weights and configuration files:
  - Weights: [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)
  - Config: [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
  - COCO Names: [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

Place all three files in the project directory.

---

## Usage

1. **Run the script**:
   ```bash
   python detect_mobile.py
   ```

2. **Live Detection**:
   - The script will start your webcam and display a live feed.
   - Mobile phones detected in the video feed will be highlighted with bounding boxes and confidence scores.

3. **Exit**:
   - Press `q` to quit the program.

---

## File Structure
```
mobile-phone-detection/
├── coco.names          # Class labels used by YOLO
├── detect_mobile.py    # Main Python script
├── yolov3.cfg          # YOLO configuration file
├── yolov3.weights      # YOLO pre-trained weights
└── README.md           # Documentation
```

---

## Example Output
When a mobile phone is detected, the program highlights it with a bounding box and displays the label `cell phone` along with the confidence score.

![Demo Output](https://via.placeholder.com/800x400?text=Add+your+output+image+here)

---

## Troubleshooting

### Common Issues
1. **Gray or blank screen**:
   - Ensure no other application is using the webcam.
   - Verify your webcam index in the code (`cap = cv2.VideoCapture(0)`).
   - Test your webcam with another application like the Windows Camera app.

2. **YOLO configuration file not found**:
   - Make sure `yolov3.weights`, `yolov3.cfg`, and `coco.names` are in the same directory as the Python script.

3. **Performance issues**:
   - Reduce the input size in the blob (e.g., `(320, 320)` to `(224, 224)`).
   - Ensure you're using a CPU-optimized version of OpenCV.

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments
- [YOLO](https://pjreddie.com/darknet/yolo/) by Joseph Redmon
- [OpenCV](https://opencv.org/) for computer vision tools
```
