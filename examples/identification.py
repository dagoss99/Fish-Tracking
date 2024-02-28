import tensorflow as tf
import os
import shutil
import numpy as np
from collections import Counter
import argparse


def find_latest_experiment(base_dir):
    track_dir = os.path.join(base_dir, 'runs', 'track')
    exp_dirs = [d for d in os.listdir(track_dir) if os.path.isdir(os.path.join(track_dir, d)) and d.startswith('exp')]
    # Sort directories by their creation time
    latest_exp_dir = sorted(exp_dirs, key=lambda x: os.path.getctime(os.path.join(track_dir, x)), reverse=True)[0]
    return latest_exp_dir

# Function to clean up the crops directory by removing folders with insufficient images
# This is because the model sometimes assigns two different IDs to the same fish for a short time
def clean_insufficient_crops(base_dir, threshold_ratio):
    latest_exp_dir = find_latest_experiment(base_dir)
    crops_dir_path = os.path.join(base_dir, 'runs', 'track', latest_exp_dir, 'crops', '0') 
    id_folders = [os.path.join(crops_dir_path, d) for d in os.listdir(crops_dir_path) if os.path.isdir(os.path.join(crops_dir_path, d))]
    
    # Count the number of images in each folder
    image_counts = {folder: len(os.listdir(folder)) for folder in id_folders}
    
    # Find the maximum number of images in a single folder to set as reference
    max_images = max(image_counts.values()) if image_counts else 0
    min_required_images = max_images * threshold_ratio
    
    # Remove folders not meeting the criteria
    for folder, count in image_counts.items():
        if count < min_required_images:
            shutil.rmtree(folder)
            #print(f"Removed {folder} due to insufficient images ({count} images).")

def parse_args():
    parser = argparse.ArgumentParser(description="Cleans up fish ID crops with insufficient images.")
    parser.add_argument('--threshold', type=float, default=0.7, help='Threshold to keep the folders (1-threshold_ratio). Default is 0.8')
    args = parser.parse_args()
    return args

def load_model(model_path):
    return tf.saved_model.load(model_path)

def preprocess_image(image_path, target_size):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.resize(img, target_size)
    img = img / 255.0  # normalize to [0,1] if necessary
    return img

def classify_image(model, image_path, target_size=(224, 224)):    
    img = preprocess_image(image_path, target_size)
    img = np.expand_dims(img, axis=0)  # model expects batch dimension
    predictions = model(img)
    #print("Raw predictions:", predictions)  # Add this line to debug
    predicted_class = np.argmax(predictions, axis=1)
    return int(predicted_class[0])



# Add this dictionary at the beginning of your script or inside the classify_fish function
class_names = {
    8: 'Black Sea Sprat',
    0: 'Gilt-Head Bream',
    5: 'Hourse Mackerel',
    2: 'Red Mullet',
    6: 'Red Sea Bream',
    1: 'Sea Bass',
    3: 'Shrimp',
    7: 'Striped Red Mullet',
    4: 'Trout'
}

def classify_fish(base_dir, model_path, threshold_ratio, target_size=(224, 224)):

    
    model = load_model(model_path)
    latest_exp_dir = find_latest_experiment(base_dir)
    crops_dir_path = os.path.join(base_dir, 'runs', 'track', latest_exp_dir, 'crops', '0') 
    id_folders = [os.path.join(crops_dir_path, d) for d in os.listdir(crops_dir_path) if os.path.isdir(os.path.join(crops_dir_path, d))]
    
    fish_results = {}
    for folder in id_folders:
        classifications = []
        for image_file in os.listdir(folder):
            image_path = os.path.join(folder, image_file)
            classification = classify_image(model, image_path, target_size)
            classifications.append(classification)
        
        # Debug: Print each classification before determining the most common one
        #print(f"Folder: {folder}, Classifications: {classifications}")

        # Determine the most common classification
        if classifications:
            most_common = Counter(classifications).most_common(1)[0][0]
            fish_id = os.path.basename(folder)
            # Debug: Print the most common classification for this folder
            #print(f"Most common classification for {fish_id}: {most_common}")
            fish_results[fish_id] = most_common
    
    results_file_path = os.path.join(base_dir, 'runs', 'track', latest_exp_dir, 'crops', '0', 'fish_classifications.txt')
    with open(results_file_path, 'w') as f:
        for fish_id, classification in fish_results.items():
            species_name = class_names.get(classification, "Unknown")  # Convert class ID to species name
            print(f"Writing to file - Fish {fish_id.replace('id_', '')}: {species_name}")
            f.write(f"Fish {fish_id.replace('id_', '')}: {species_name}\n")


if __name__ == "__main__":
    args = parse_args()
    threshold_ratio = 1 - args.threshold

    base_dir = os.getcwd()
    model_path = os.path.join(base_dir, 'species_model')

    clean_insufficient_crops(base_dir, threshold_ratio)
    classify_fish(base_dir, model_path, threshold_ratio)
