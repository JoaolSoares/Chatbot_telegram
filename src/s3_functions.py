# Imports
import  json
from    defines     import *

def read_object(obj):
    try:
        response = s3.get_object(Bucket=bucket, Key=obj)
        json_data = json.loads(response['Body'].read().decode('utf-8'))
    except:
        json_data = []
    return (json_data)
