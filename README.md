# The training_YOLO branch is specifically created to facilitate the development and training of YOLO models as per the user's requirements.

## Getting Started

The notebook has been run on Kaggle: <a href="https://www.kaggle.com/code/fabiodagostino/fish-detection-yolo"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>

The notebook is structured such that it's easy to reproduce by following the different steps. This facilitates the training of YOLO which is the Multi-Object-Tracking algorithm used in the main branch to run the classification methods described. Once you trained the model, download the weights and place them in the folder where you have cloned the main branch. 

## Usage

To train YOLO, prepare the data by adhering to the YOLO labeling format, then organize the folders as follows and properly modify the creation of the .yaml file on the notebook:

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

