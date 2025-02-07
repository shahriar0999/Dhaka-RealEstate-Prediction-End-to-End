import pathlib
import os
import src

PACKAGE_ROOT = pathlib.Path(src.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

FILE_NAME_HOUSE_RENT = "house_rent_price_prediction.csv"
FILE_NAME_HOUSE_PRICE = "House_Price_dataset.csv"

TEST_FILE_HOUSE_RENT  = "test_data_house_rent.csv"
TEST_FILE_HOUSE_PRICE  = "test_data_house_price.csv"

MODEL_NAME_FOR_HOUSE_RENT = "regressionModel_HouseRent.pkl"
MODEL_NAME_FOR_HOUSE_PRICE = "regressionModel_HousePrice.pkl"

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = "price"

# Final features used for model training
FEATURES = ['city_location', 'block_sector', 'bedroom', 'bathroom',
       'sqrtFeet', 'price']

PRED_FEATURES = ['city_location', 'block_sector', 'bedroom', 'bathroom', 'sqrtFeet']

# Categorical features
CAT_FEATURES = ['city_location', 'block_sector']

# Numerical features
NUM_FEATURES = ['bedroom', 'bathroom', 'sqrtFeet']

# Features to be dropped
DROP_FEATURES = 'price'

# Features to be scaled and i think after transform categorical features it also need to be scaled
SCALED_FEATURES = ['bedroom', 'bathroom', 'sqrtFeet']

# Features to be encoded
ENCODE_FEATURES = ['city_location', 'block_sector']

# Features to be transformed
TRANSFORM_FEATURES = ['city_location', 'block_sector']
