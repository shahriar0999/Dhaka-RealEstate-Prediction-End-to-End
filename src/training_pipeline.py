import pandas as pd
import numpy as np
from pathlib import Path
import os
import sys
import joblib


# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.config import config
from src.pre_processing.data_handling import load_dataset, save_pipeline,  separate_x_y, split_dataset
import src.pre_processing.preprocessing as pp
from src.upload_to_s3.uploadModel import upload_model_to_s3
import src.pipeline as pipe
import sys

def perform_training_for_houseRent():
    # load dataset
    data = load_dataset(config.FILE_NAME_HOUSE_RENT)

    # seperate x and y
    X, y = separate_x_y(data)

    # split dataset
    X_train, X_test, y_train, y_test = split_dataset(data)

    test_data = X_test.copy()
    test_data[config.TARGET] = y_test

    # save test data
    test_data.to_csv(os.path.join(config.DATAPATH,config.TEST_FILE_HOUSE_RENT))

    # train model
    pipe.regression_pipeline_for_houseRent.fit(X_train, y_train)

    # save model
    # save_pipeline(pipe.regression_pipeline_for_houseRent, config.MODEL_NAME_FOR_HOUSE_RENT)

    # here i want to upload that model s3 instade of saving it locally
    upload_model_to_s3(pipe.regression_pipeline_for_houseRent, 'newbucket29382', 's3_model_from_trainStage/houseRent.pkl')


def perform_training_for_housePrice():
    # load dataset
    data = load_dataset(config.FILE_NAME_HOUSE_PRICE)

    # seperate x and y
    X, y = separate_x_y(data)

    # split dataset
    X_train, X_test, y_train, y_test = split_dataset(data)

    test_data = X_test.copy()
    test_data[config.TARGET] = y_test

    # save test data
    test_data.to_csv(os.path.join(config.DATAPATH,config.TEST_FILE_HOUSE_PRICE))

    # train model
    pipe.regression_pipeline_for_housePrice.fit(X_train, y_train)

    # save model
    # save_pipeline(pipe.regression_pipeline_for_housePrice, config.MODEL_NAME_FOR_HOUSE_PRICE)

    # first serialize the model
    model = pipe.regression_pipeline_for_housePrice

    # here i want to upload that model s3 instade of saving it locally
    upload_model_to_s3(pipe.regression_pipeline_for_housePrice, 'newbucket29382', 's3_model_from_trainStage/housePrice.pkl')

if __name__ == "__main__":
    perform_training_for_houseRent()
    perform_training_for_housePrice()