from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from io import BytesIO
import boto3
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.config import config
from src.pre_processing.data_handling import load_dataset, save_pipeline,  separate_x_y, split_dataset

s3 = boto3.client('s3')
bucket_name = 'newbucket29382'

# now directly load the model from s3 instead of saving it locally
def load_model_from_s3(bucket, key):
    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        model_data = obj['Body'].read()
        model = joblib.load(BytesIO(model_data))
        print(f"Model loaded from s3://{bucket}/{key}")
        return model
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None

# load model pipeline for house_rent

regression_pipeline_houseRent = load_model_from_s3(bucket_name, 's3_model_from_trainStage/houseRent.pkl')

def generate_predictions_for_houseRent():
    test_data = load_dataset(config.TEST_FILE_HOUSE_RENT)
    X,y = separate_x_y(test_data)
    pred = regression_pipeline_houseRent.predict(X)
    # accuracy metrics
    mse = mean_squared_error(y, pred)
    r2 = r2_score(y, pred)
    print(f'Root Mean Squared Error of HouseRent Model: {np.sqrt(mse)}')
    print(f'R2 Score of HouseRent Model: {r2}')

#predict individual house rent : bedroom	bathroom	sqrtFeet	
feature_r = {
    'city_location': 5,
    'block/sector': 114,
    'bedroom': 3,
    'bathroom': 3,
    'sqrtFeet': 1340
 }

def predict_house_rent(feature):
    data = pd.DataFrame([feature])
    pred = regression_pipeline_houseRent.predict(data)
    print(f'Predicted House Rent: {pred[0]}')
    return pred

#############################
#############################
# load pipeline for house_price
regression_pipeline_housePrice = load_model_from_s3(bucket_name, 's3_model_from_trainStage/housePrice.pkl')


def generate_predictions_for_housePrice():
    test_data = load_dataset(config.TEST_FILE_HOUSE_PRICE)
    X,y = separate_x_y(test_data)
    pred = regression_pipeline_housePrice.predict(X)
    # accuracy metrics
    mse = mean_squared_error(y, pred)
    r2 = r2_score(y, pred)
    print(f'Root Mean Squared Error of HousePrice Model: {np.sqrt(mse)}')
    print(f'R2 Score of HousePrice Model: {r2}')

#predict individual house rent : bedroom	bathroom	sqrtFeet	
feature_p = {
    'city_location': 5,
    'block/sector': 114,
    'bedroom': 3,
    'bathroom': 3,
    'sqrtFeet': 1340
 }

def predict_house_price(feature):
    data = pd.DataFrame([feature])
    pred = regression_pipeline_housePrice.predict(data)
    print(f'Predicted House Price: {pred[0]}')
    return pred

if __name__=='__main__':
    generate_predictions_for_houseRent()
    predict_house_rent(feature_r)
    generate_predictions_for_housePrice()
    predict_house_price(feature_p)