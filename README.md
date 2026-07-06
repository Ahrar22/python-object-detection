# Python Automation - Speed Detector

A real-time object tracking and speed estimation application that utilizes your webcam feed[span_0](start_span)[span_0](end_span). The project leverages the **YOLOv8** object detection model and **OpenCV** to track moving objects and estimate their speed as they cross a designated line[span_1](start_span)[span_1](end_span).

---

## 🚀 Features

* **Real-time Tracking:** Uses the pre-trained `yolov8n.pt` (nano) model to efficiently detect and track objects with persistent tracking enabled[span_2](start_span)[span_2](end_span).
* **Speed Estimation:** Utilizes Ultralytics' built-in speed estimation solution, calculating speed via a virtual line placed horizontally across the middle of the screen[span_3](start_span)[span_3](end_span).
* **Mirror Effect:** Automatically flips the webcam frame horizontally for a more natural mirror viewing experience[span_4](start_span)[span_4](end_span).
* **Optimized Performance:** Runs object tracking at an image size of 320 pixels (`imgsz=320`) to maintain a smooth and responsive frame rate[span_5](start_span)[span_5](end_span).

---

## 🛠 Prerequisites & Installation

Before running the script, make sure you have Python installed. You will need to install the `ultralytics` package (which includes YOLOv8) and `opencv-python`[span_6](start_span)[span_6](end_span).

You can install the required dependencies using pip:

```bash
pip install ultralytics opencv-python
