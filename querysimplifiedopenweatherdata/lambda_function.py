import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('simplifiedopenweatherdata')
    response = table.scan(Select="ALL_ATTRIBUTES")
    result=response['Items']



    return {
        'statusCode': 200,
        'body': result
    }
