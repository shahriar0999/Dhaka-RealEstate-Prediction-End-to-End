import boto3
import os
import joblib
from pathlib import Path
from io import BytesIO

bucket_name = "newbucket29382"
s3 = boto3.client('s3')



def load_model_from_s3(key, bucket=bucket_name):
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        buffer = BytesIO(response['Body'].read())
        model = joblib.load(buffer)
        return model
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")
        return None