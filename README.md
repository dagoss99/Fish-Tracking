# The training_YOLO branch is specifically created to facilitate the development and training of YOLO models as per the user's requirements.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/fish-classification-project.git
```
2. Check into training_YOLO:
```
git checkout training_YOLO
```
2. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

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

