import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from src.config import config
from src.pre_processing.data_handling import load_dataset

# write preprocessing functions here so that i can apply into pipeline

# data = load_dataset(config.FILE_NAME)
# data = data[config.FEATURES]

# # Custom Categorical Encoder
# def CustomEncoder(columns):
#     encode = OrdinalEncoder()
#     data[columns] = encode.fit_transform(data[columns])
#     return data

# # Custom Scaler
# def CustomScaler(columns):
#     scale = StandardScaler()
#     data[columns] = scale.fit_transform(data[columns])
#     return data
# preprocessing.py (or your custom module)
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

class CustomEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.encoder = OrdinalEncoder()

    def fit(self, X, y=None):
        # Fit the encoder on the specified columns
        self.encoder.fit(X[self.columns])
        return self

    def transform(self, X):
        # Apply ordinal encoding
        X_transformed = X.copy()
        X_transformed[self.columns] = self.encoder.transform(X_transformed[self.columns])
        return X_transformed

class CustomScaler(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.scaler = StandardScaler()

    def fit(self, X, y=None):
        # Fit the scaler on the specified columns
        self.scaler.fit(X[self.columns])
        return self

    def transform(self, X):
        # Apply scaling
        X_transformed = X.copy()
        X_transformed[self.columns] = self.scaler.transform(X_transformed[self.columns])
        return X_transformed