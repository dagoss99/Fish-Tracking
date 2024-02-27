# Fish Classification and Detection Project

Exploring innovative fish classification using YOLO for object tracking and DeepLabCut for trajectory analysis. Aims to lay groundwork for future aquatic life monitoring through deep learning.

## Demo Video

[![Demo Video](https://youtu.be/CnK_N_VXnho/0.jpg)](https://youtu.be/CnK_N_VXnho) "Fish Detection and Classification Demo")

## Project Overview

This project delves into the challenges of fish detection and classification by harnessing the power of deep learning techniques. The primary objectives are twofold:

1. **Fish Detection and Real-Time Classification using YOLO:** Utilizing the You Only Look Once (YOLO) framework, the project offers a robust solution for real-time object tracking, enabling accurate and efficient fish detection in video footage.

2. **Species Classification:** By capturing multiple snapshots of detected fishes, the project employs a novel classification method. It aggregates predictions across these images, determining the species based on the majority vote, ensuring high accuracy and reliability.

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

## Usage

Provide instructions on how to use the project, including any necessary commands or scripts.

## Data

To train YOLO, prepare the data by adhering to the YOLO format, the organise the folders as follow and properly modify the creation of the .yaml file on the yolo-training.ipynb notebook:

```
data
|——————train 
|        └——————images
|        └——————labels
|——————val
|        └——————images
|        └——————labels
```


## Citation
See BoxMOT and Ultralyrics repositories, which we base our work upon: 
- Broström, M. BoxMOT: pluggable SOTA tracking modules for object detection, segmentation and pose estimation models (Version 10.0.43) [Computer software]. https://doi.org/https://zenodo.org/record/7629840
- Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics

