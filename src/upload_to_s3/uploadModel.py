from pathlib import Path
import pickle
import os
import sys
import boto3

# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')
sys.path.append(str(PACKAGE_ROOT))

# upload model to s3
def upload_model_to_s3(model_data, bucket, key):
    s3 = boto3.client('s3')
    model = pickle.dumps(model_data)
    s3.put_object(Bucket=bucket, Key=key, Body=model)
    print(f"Model uploaded to s3")




