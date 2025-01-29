from sklearn.pipeline import Pipeline
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.config import config
from src.pre_processing.preprocessing import CustomEncoder, CustomScaler
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Best Parameters: {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 120}
# Best R2 Score: 0.8615973827388711


# regression_pipeline = Pipeline(
#     [
#         ('ordinal_encoder', pp.CustomEncoder(config.ENCODE_FEATURES)),
#         ('ordinal_encod_scale', pp.CustomScaler(config.TRANSFORM_FEATURES)),
#         ('scaler', pp.CustomScaler(config.SCALED_FEATURES)),
#         ('regressor', RandomForestRegressor(max_depth=20, min_samples_leaf=2, min_samples_split=2, n_estimators=120))
#     ]
# )

regression_pipeline = Pipeline(
    [
        # Use instances of the classes
        ('ordinal_encod_scale', CustomScaler(config.TRANSFORM_FEATURES)),
        ('scaler', CustomScaler(config.SCALED_FEATURES)),
        ('regressor', RandomForestRegressor(max_depth=20, min_samples_leaf=2, min_samples_split=2, n_estimators=120))
    ]
)