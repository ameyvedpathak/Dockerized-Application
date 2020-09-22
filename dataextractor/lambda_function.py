import boto3
# import os
# import sys
# import uuid
from urllib.parse import unquote_plus
# from PIL import Image
# import PIL.Image

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        print("Records:",record)
        print("Bucket:",bucket)
        print("Key:",key)

        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, key)
        file_content = obj.get()['Body'].read().decode('utf-8')
        res=(eval(file_content))
        data=res['list']
        # for i in range(len(data)):
        #     print(data[i]['name'])
        #     print(data[i]['weather'][0])

        ######## Table creation########
        # client = boto3.client('dynamodb', region_name='us-east-1')
        # try:
        #     resp = client.create_table(
        #         TableName="simplifiedopenweatherdata",
        #         KeySchema=[
        #             {
        #                 "AttributeName": "name",
        #                 "KeyType": "HASH"
        #             }
        #         ],
        #         AttributeDefinitions=[
        #             {
        #                 "AttributeName": "name",
        #                 "AttributeType": "S"
        #             }
        #         ],
        #         ProvisionedThroughput={
        #             "ReadCapacityUnits": 1,
        #             "WriteCapacityUnits": 1
        #         }
        #     )
        #     print("Table created successfully!")
        # except Exception as e:
        #     print("Error creating table:")
        #     print(e)

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('simplifiedopenweatherdata')

        for i in range(len(data)):
            with table.batch_writer() as batch:
                batch.put_item(Item={"name": data[i]['name'], "weather": data[i]['weather'][0]})



        result=[]
        for i in range(len(data)):
            resp=(table.get_item(Key={"name": data[i]['name']}))
            result.append(resp['Item'])

        print(result)

        # tmpkey = key.replace('/', '')
        # download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        # upload_path = '/tmp/resized-{}'.format(tmpkey)
        # s3_client.download_file(bucket, key, download_path)
        # resize_image(download_path, upload_path)
        # s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)
