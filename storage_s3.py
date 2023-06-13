import boto3
import os
import os.path
import configparser
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError

session = boto3.Session(
    aws_access_key_id="AKIAVHUOMMKBZXHORDVB",
    aws_secret_access_key="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"
    )

open_data_bucket = 'hajarbucketaws'
s3 = session.resource('s3')

s3.Bucket(open_data_bucket).upload_file('/home/ubuntu/data_Ex/data_Ex/data_clear.csv', 'donnees.csv')
