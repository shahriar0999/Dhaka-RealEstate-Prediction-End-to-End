import os
import sys
import pickle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aws_s3 import download_model

force_download = False


# Construct the full path to the file
local_path = 'ml-models'
file_name = 'regressionModel_HousePrice.pkl'
# Construct the full path to the file
file_path = os.path.join(local_path, file_name)

if not os.path.isfile(file_path) or force_download:
    download_model("s3_model/regressionModel_HousePrice.pkl")
    print("Model downloaded successfully")

# now load the model eg .pkl file without using with statement
open_model = open(file_path, 'rb')
house_price_model = pickle.load(open_model)



# house rent model
file_name = 'regressionModel_HouseRent.pkl'
# Construct the full path to the file
file_path = os.path.join(local_path, file_name)

if not os.path.isfile(file_path) or force_download:
    download_model("s3_model/regressionModel_HouseRent.pkl")
    print("Model downloaded successfully")

# now load the model eg .pkl file without using with statement
open_model = open(file_path, 'rb')
house_rent_model = pickle.load(open_model)

