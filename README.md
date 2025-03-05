# Real-Time Object Detection using YOLOv8

## Project Overview
This project implements a real-time object detection system using the YOLOv8 model with OpenCV. The system captures live video from a webcam, processes each frame using YOLOv8, and overlays bounding boxes on detected objects. The goal is to provide efficient and accurate real-time object detection for various applications, including surveillance, autonomous systems, and AI-driven analytics.

## Features
- **Real-time object detection** using the YOLOv8 model.
- **Webcam integration** for live video processing.
- **Optimized for CPU usage**, making it accessible for lower-end devices.
- **Customizable settings** to modify detection parameters.
- **Efficient frame processing** with optimized image size for faster inference.
- **User-friendly controls** to exit the detection window easily.

## Installation & Setup
Ensure you have Python installed, then install the required dependencies:

```bash
pip install ultralytics opencv-python
```

### Steps to Run
1. Clone the repository (if applicable) or download the script.
2. Place the `yolov8s.pt` model file in the same directory as the script.
3. Run the script using:

```bash
python experiment.py
```

### Controls
- Press `q` to exit the program.

## Notes
- The script uses `imgsz=320` to optimize performance by resizing the input frame.
- Ensure your webcam is properly connected and accessible.
- You can modify the model parameters and visualization settings to suit your needs.

## License
This project is under MIT License and free to use. Modify as needed!

## Contact
For any queries, improvements, or collaborations, feel free to reach out:
- **Email:** nsachdeva300@gmail.com
- **GitHub:** https://github.com/Codenaman21
- **LinkedIn:** https://www.linkedin.com/in/naman-sachdeva-9a70a5335/

Happy coding! 🚀

