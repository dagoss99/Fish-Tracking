import argparse
import os
from pathlib import Path
import subprocess

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Run tracking and classification on a video source.")
    parser.add_argument('--source', type=str, help='Path to the video file.')
    parser.add_argument('--yolo-model', type=str, help='Path to the YOLO model file.')
    return parser.parse_args()

# Function to run tracking
def run_tracking(source, yolo_model):
    # Assuming track.py is in the examples directory relative to this script
    track_py_path = Path(__file__).parent / 'examples' / 'track.py'
    tracking_method = 'ocsort'
    command = [
        'python', str(track_py_path),
        '--source', source,
        '--tracking-method', tracking_method,
        '--show',
        '--yolo-model', yolo_model,
        '--save',
        '--save-id-crops'
    ]
    subprocess.run(command, check=True)

# Function to run identification
def run_identification():
    # Assuming identification.py is in the examples directory relative to this script
    identification_py_path = Path(__file__).parent / 'examples' / 'identification.py'
    command = ['python', str(identification_py_path)]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    args = parse_args()
    
    # Run tracking
    print("Running tracking...")
    run_tracking(args.source, args.yolo_model)
    
    # Run classification
    print("Running classification...")
    run_identification()

    print("Process completed.")
