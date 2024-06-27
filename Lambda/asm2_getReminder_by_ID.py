import json
import boto3
client = boto3.client('dynamodb')
def lambda_handler(event, context):
  GetItem = client.get_item(
    TableName='asm2-ccp302x',
    Key={
        'id': {
          'S': '1'
        }
    }
  )
  response = {
      'statusCode': 200,
      'body': json.dumps(GetItem)
  }

  return response