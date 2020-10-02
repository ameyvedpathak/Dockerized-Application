import json
import boto3
import time
from urllib.request import urlopen


def lambda_handler(event, context):
    #reading the reponse from API and storing it in result
    with urlopen('https://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=dbd0fa9b51e547498be8c1c1febfcb2d') as url:
        http_info = url.info()
        raw_data = url.read().decode(http_info.get_content_charset())
    project_info = json.loads(raw_data)
    result = {'headers': http_info.items(), 'body': project_info}
    print(result['body'])
##step1 navigate to s3 bucket
##step2 save the request body to new file in s3 bucket
    s3 = boto3.resource('s3')
    content=str(result['body'])
    timestr = time.strftime("%Y%m%d-%H%M%S") # using timestamp format for file name
    s3.Object('localopenweatherdata', timestr).put(Body=content)# pushing file in s3 bucket

    return None
