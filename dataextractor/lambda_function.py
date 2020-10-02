import boto3
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        print("Records:",record) ## grabing the records
        print("Bucket:",bucket)  ## and printing the
        print("Key:",key)        ## details of bucket

        s3 = boto3.resource('s3')
        obj = s3.Object(bucket, key) # getting the files from S3 bucket
        file_content = obj.get()['Body'].read().decode('utf-8')
        res=(eval(file_content))
        data=res['list']
############ Can use this code to create table ################################
# This is just a simple use of python to create dynamoDB table
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
#################################################################################

# specifying table name and region
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('simplifiedopenweatherdata')

# writing operation to table
        for i in range(len(data)):
            with table.batch_writer() as batch:
                batch.put_item(Item={"name": data[i]['name'], "weather": data[i]['weather'][0]})
# printing the table just to check the contents
        result=[]
        for i in range(len(data)):
            resp=(table.get_item(Key={"name": data[i]['name']}))
            result.append(resp['Item'])

        print(result)
return None
