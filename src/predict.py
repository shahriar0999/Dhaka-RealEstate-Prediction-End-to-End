from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.config import config
from src.pre_processing.data_handling import load_dataset, save_pipeline,  separate_x_y, split_dataset

# load pipeline
model_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
regression_pipeline = joblib.load(model_path)

def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    X,y = separate_x_y(test_data)
    pred = regression_pipeline.predict(X)
    # accuracy metrics
    mse = mean_squared_error(y, pred)
    r2 = r2_score(y, pred)
    print(f'Root Mean Squared Error: {np.sqrt(mse)}')
    print(f'R2 Score: {r2}')

#predict individual house rent bedroom	bathroom	sqrtFeet	
feature = {
    'city_location': 5,
    'block/sector': 114,
    'bedroom': 3,
    'bathroom': 3,
    'sqrtFeet': 1340
 }

def predict_house_price(feature):
    data = pd.DataFrame([feature])
    pred = regression_pipeline.predict(data)
    print(f'Predicted House Rent: {pred[0]}')
    return pred

if __name__=='__main__':
    generate_predictions()
    predict_house_price(feature)