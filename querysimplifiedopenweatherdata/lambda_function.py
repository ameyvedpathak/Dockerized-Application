import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('simplifiedopenweatherdata')
    result=[]
    for i in range(len(data)):
        resp=(table.get_item(Key={"name": data[i]['name']}))
        result.append(resp['Item'])



    return {
        'statusCode': 200,
        'body': result
    }
