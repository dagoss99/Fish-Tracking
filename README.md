# The training_YOLO branch is specifically created to facilitate the development and training of YOLO models as per the user's requirements.

## Getting Started

The notebook has been run on Kaggle: <a href="https://www.kaggle.com/code/fabiodagostino/fish-detection-yolo"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>

This comprehensive notebook guides users through the setup, training, and validation of the YOLO (You Only Look Once) model for Multi-Object Tracking. Starting from environment setup in Kaggle, it covers directory management, model loading with Ultralytics, YAML configuration, and detailed steps for model training and validation. The notebook includes practical code snippets for importing essential libraries, data preparation, and visualization techniques to assess model performance. After successfully training the model, download the trained weights and place them in the folder of your project the trained weights into your project. This structured approach simplifies the complex process of training YOLO models, making it accessible for users to replicate and apply in their object detection tasks.

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


## Acknowledgement
Thanks to the well made tutorial:
- https://github.com/Spacewalker69/Yolov8_Tutorial_Fish_Detection/tree/5c664a553dd4e29e0d5ae7e99dfb6d83ffdc9da7

