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
    s3.put_object(Bucket=bucket_name, Key=key, Body=model)
    print(f"Model uploaded to s3://{bucket}/{key}")

s3 = boto3.client('s3')
bucket_name = 'newbucket29382'

def upload_directory(directory_path, s3_prefix):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file).replace("\\", "/")
            relpath = os.path.relpath(file_path, directory_path)
            s3_key = os.path.join(s3_prefix, relpath).replace("\\", "/")
            
            s3.upload_file(file_path, bucket_name, s3_key)




if __name__ == "__main__":
    upload_directory(MODEL_PATH, 's3_model')



