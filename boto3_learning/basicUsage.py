import sys

from boto3.session import Session
import boto3

aws_key = ''
aws_secret = ''

session = Session(aws_access_key_id=aws_key,aws_secret_access_key=aws_secret,region_name='')