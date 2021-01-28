import boto3 
import json

def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    filename = event["Records"][0]["s3"]["object"]["key"]

    json_object = boto3.client("s3").get_object(
        Bucket = bucket, 
        Key = filename 
    )

    json_parse = json_object["Body"].read()
    json_diction = json.loads(json_parse)

    print(json_diction)

    transactions = json_diction["Transactions"]
    
    for t in transactions:
        print(t["TransactionType"])
    return "Sucess!"


