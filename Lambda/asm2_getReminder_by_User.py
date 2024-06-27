import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event,context):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('asm2-ccp302x')
  
  
  response = table.scan(
      FilterExpression=Attr('user_email').eq('thangfoseca@gmail.com')
  )
  items = response['Items']
  print(items)
  return response
