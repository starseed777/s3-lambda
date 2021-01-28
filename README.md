This is a personal passion project / / 
json-uploader.py file will take all transaction JSON files from the current directory and will upload them all to an existing s3 bucket.  

Then after configuring the s3 put object event for the lambda function >> the s3-file-processor.py file will take those JSON transaction files and parse them + convert them into a dictionary structure then prints in that form so when going through the cloudwatch logs it will show purchases + refund amounts.

