# Fish Classification and Detection Project

Exploring innovative fish classification using YOLO for object tracking and DeepLabCut for trajectory analysis. Aims to lay groundwork for future aquatic life monitoring through deep learning.

## Project video

The following video explains the motivation and methodologies of the project

[![Exploration of classification techniques for fish species detection in underwater enviroments](https://github.com/dagos99/Fish-Tracking/blob/main/assets/images/thumbnail.jpg)](https://www.youtube.com/watch?v=q6aBy1VgHOA)


## Demo Video

[![Demo Video](https://youtu.be/CnK_N_VXnho/0.jpg)](https://youtu.be/CnK_N_VXnho) A demo of the first methodology.

## Project Overview

This project delves into the challenges of fish detection and classification by harnessing the power of deep learning techniques. The primary objectives are twofold:

1. **Fish Detection and Real-Time Classification using YOLO:** Utilizing the You Only Look Once (YOLO) framework, the project offers a robust solution for real-time object tracking, enabling accurate and efficient fish detection in video footage. Trained with a specific dataset of species indigenous of Côte D'Azur. 

2. **Species Classification:** By capturing multiple snapshots of detected fishes, the project employs a novel classification method. It aggregates predictions across these images, determining the species based on the majority vote, ensuring high accuracy and reliability. Trained on the dataset [A Large-Scale Dataset for Fish Segmentation and Classification](https://ieeexplore.ieee.org/document/9259867).

3. **DeepLabCut for Trajectory Analysis:** In a pioneering exploration, the project uses DeepLabCut to analyze the trajectory of fish body parts. This method opens new avenues for understanding fish behavior and movement patterns, contributing valuable insights for species classification.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/fish-classification-project.git
```
2. Install the required packages:
```
pip install -r requirements.txt
```

# Usage

## The following commands can be used to test the different methods (you can add "--save" to the commands to save the video in the runs folder):

### Just tracking without classification
```
python examples/track.py --source videos/track.mp4 --tracking-method strongsort --show --yolo-model models/fish_yolov8_158_epochs.pt 
```

### Method 1: Real time classification while tracking
```
python examples/track.py --source videos/method1.mp4 --tracking-method strongsort --show --yolo-model models/yolov8_custom_30epochs.pt 
```

### Method 2: Offline classification after tracking 
```
python track+classification.py --source videos/method2.mp4 --yolo-model models/fish_yolov8_158_epochs.pt
```



## Citation
See BoxMOT and Ultralyrics repositories, which we base our work upon: 
- Broström, M. BoxMOT: pluggable SOTA tracking modules for object detection, segmentation and pose estimation models (Version 10.0.43) [Computer software]. https://doi.org/https://zenodo.org/record/7629840
- Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics

