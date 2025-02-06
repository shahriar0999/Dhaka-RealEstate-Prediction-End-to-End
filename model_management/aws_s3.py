import boto3
import os

bucket_name = "newbucket29382"
s3 = boto3.client('s3')



def download_model(file_name):
    # Make sure the local directory exists
    local_dir = 'ml-models'
    os.makedirs(local_dir, exist_ok=True)

    # Define the path where the file should be saved
    local_file_path = os.path.join(local_dir, file_name.split('/')[-1])
    
    s3.download_file(bucket_name, file_name, local_file_path)
