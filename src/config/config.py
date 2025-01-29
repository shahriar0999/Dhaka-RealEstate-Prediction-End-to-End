import pathlib
import os
import src

PACKAGE_ROOT = pathlib.Path(src.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

FILE_NAME = "house_rent_price_prediction.csv"

TEST_FILE = "test_data.csv"

MODEL_NAME = "regressionModel.pkl"

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = "price"

# Final features used for model training
FEATURES = ['city_location', 'block/sector', 'bedroom', 'bathroom',
       'sqrtFeet', 'price']

PRED_FEATURES = ['city_location', 'block/sector', 'bedroom', 'bathroom', 'sqrtFeet']

# Categorical features
CAT_FEATURES = ['city_location', 'block/sector']

# Numerical features
NUM_FEATURES = ['bedroom', 'bathroom', 'sqrtFeet']

# Features to be dropped
DROP_FEATURES = 'price'

# Features to be scaled and i think after transform categorical features it also need to be scaled
SCALED_FEATURES = ['bedroom', 'bathroom', 'sqrtFeet']

# Features to be encoded
ENCODE_FEATURES = ['city_location', 'block/sector']

# Features to be transformed
TRANSFORM_FEATURES = ['city_location', 'block/sector']




