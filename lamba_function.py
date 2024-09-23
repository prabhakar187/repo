import json
import boto3
import os

def lambda_handler(event, context):
    # Get the bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Create S3 client
    s3 = boto3.client('s3')

    # Get the object type (content type)
    response = s3.head_object(Bucket=bucket, Key=key)
    content_type = response['ContentType']

    # Return the content type
    return {
        'statusCode': 200,
        'body': json.dumps({
            'bucket': bucket,
            'key': key,
            'content_type': content_type
        })
    }
