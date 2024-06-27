import json
import boto3
import datetime,time

client = boto3.client('dynamodb')
def lambda_handler(event, context):
    print(event)
    expiryTimestamp = int(time.time() + 5)
    PutItem = client.put_item(
        TableName='asm2-ccp302x',
        Item={
            'id': {
              'S': '1'
            },
            'ttl': {
                'N': str(expiryTimestamp)
            },
            'user_email':{
                'S':'thangfoseca@gmail.com'
            },
            'message':{
                'S':'Publish next Youtube Video'
            }
        }
      )
     
    response = {
      'statusCode': 200,
      'body': json.dumps(PutItem)
    }
    return response