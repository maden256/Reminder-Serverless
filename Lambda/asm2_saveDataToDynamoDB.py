import json
import boto3
import datetime,time

client = boto3.client('dynamodb')
def lambda_handler(event, context):
    print(event)
    #expiryTimestamp = int(time.time() + 300)
    if event['Records'][0]['eventName'] == "REMOVE":
        id = event['Records'][0]['dynamodb']['OldImage']['id']['S']
        email = event['Records'][0]['dynamodb']['OldImage']['user_email']['S']
        message = event['Records'][0]['dynamodb']['OldImage']['message']['S']
        PutItem = client.put_item(
            TableName='asm2-ccp302x',
            Item={
                'id': {
                  'S': str(id)
                },
                'user_email':{
                    'S': str(email)
                },
                'message':{
                    'S': str(message)
                }
            }
          )
         
        response = {
          'statusCode': 200,
          'body': json.dumps(PutItem)
        }
        return response