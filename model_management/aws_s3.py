import boto3
import os
import joblib
from pathlib import Path
from io import BytesIO

bucket_name = "newbucket29382"
s3 = boto3.client('s3')



def download_model(file_name):
    # Make sure the local directory exists
    local_dir = 'ml-models'
    os.makedirs(local_dir, exist_ok=True)

    # Define the path where the file should be saved
    local_file_path = os.path.join(local_dir, file_name.split('/')[-1])
    
    s3.download_file(bucket_name, file_name, local_file_path)

# def load_model_from_s3(bucket, key):
#     try:
#         obj = s3.get_object(Bucket=bucket, Key=key)
#         model_data = obj['Body'].read()
#         # model = joblib.load(BytesIO(model_data))
#         return model_data
#     except Exception as e:
#         print(f"An error occurred while loading the model: {e}")
#         return None


def load_model_from_s3(bucket, key):
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        buffer = BytesIO(response['Body'].read())
        model = joblib.load(buffer)
        return model
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None