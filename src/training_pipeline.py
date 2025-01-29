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
import src.pipeline as pipe
import sys

def perform_training():
    # load dataset
    data = load_dataset(config.FILE_NAME)

    # seperate x and y
    X, y = separate_x_y(data)

    # split dataset
    X_train, X_test, y_train, y_test = split_dataset(data)

    test_data = X_test.copy()
    test_data[config.TARGET] = y_test

    # save test data
    test_data.to_csv(os.path.join(config.DATAPATH,config.TEST_FILE))

    # train model
    pipe.regression_pipeline.fit(X_train, y_train)

    # save model
    save_pipeline(pipe.regression_pipeline)

if __name__ == "__main__":
    perform_training()