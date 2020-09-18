Backend workflow:
1. Hit the API of openweather.org
2. Collect the Json response and dump to S3 bucket in a file. (always create a new file with format: time.time())
3. Trigger an event on file creation.
4. Read the file on event, extract following attributes
   1. Name
   2. Weather { }
5. Store the data in DynamoDB table


UI workflow:
1. Using JS, hit the URL of API gateway
2. read all the data from dynamoDB table and return as Json response
3. get the json response and display in tabular format in HTML