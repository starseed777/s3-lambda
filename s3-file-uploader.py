from secrets import access_key , secret_access_key, bucket

import boto3
import os 

client = boto3.client("s3",
                        aws_access_key_id = access_key ,
                        aws_secret_access_key = secret_access_key)

for file in os.listdir():

    if ".py" in file:
        upload_bucket = bucket
        upload_file = 'PYTHON/' +  str(file)
        client.upload_file(file, upload_bucket, upload_file)
        print("successfully uploaded all python files to s3")

    elif ".json" in file:
        upload_bucket = bucket
        upload_file = 'JSON/' +  str(file)
        client.upload_file(file, upload_bucket, upload_file)
        print("successfully uploaded all JSON files to s3")
    
