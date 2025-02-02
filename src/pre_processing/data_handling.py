import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from pathlib import Path
import sys


PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from src.config import config

# load dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH, file_name)
    data = pd.read_csv(filepath)
    data.columns = [col.strip() for col in data.columns]
    return data[config.FEATURES]

# seperate x and y
def separate_x_y(data):
    X = data.drop(config.TARGET, axis=1)
    y = data[config.TARGET]
    return X, y

# split dataset
def split_dataset(data, test_size=0.25, random_state=5):
    X, y = separate_x_y(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

# serialization
import os
from joblib import dump

def save_pipeline(pipeline_to_save, model_name):
    save_path = os.path.join(config.SAVE_MODEL_PATH, model_name)
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # <-- Key fix
    
    # Save the pipeline
    dump(pipeline_to_save, save_path)
    print(f"Model saved at: {save_path}")

# deserialization
def load_pipeline(pipeline_to_load):
    # Construct the full path to the model file
    save_path = os.path.join(config.SAVE_MODEL_PATH, pipeline_to_load)
    
    # Check if the file exists
    if not os.path.exists(save_path):
        raise FileNotFoundError(f"Model file not found at: {save_path}")
    
    # Load the model
    model_loaded = joblib.load(save_path)
    print(f"Model loaded from: {save_path}")
    return model_loaded