import json
import boto3

def lambda_handler(event, context):
## Reading all the contents of table and passing it on to body in result
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('simplifiedopenweatherdata')
    response = table.scan(Select="ALL_ATTRIBUTES")
    result=response['Items']

    return {
        'statusCode': 200,
        'body': result
    }
