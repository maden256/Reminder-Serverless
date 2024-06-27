import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('asm2-ccp302x')

def lambda_handler(event, context):
    # Get ID from query parameters
    id = event['queryStringParameters']['id']

    # Retrieve item from DynamoDB
    response = table.get_item(Key={'id': id})
    item = response.get('Item', None)

    if item:
        # Modify information
        # For example, update a specific attribute
        item['attribute_to_update'] = 'new_value'

        # Update item in DynamoDB
        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps('Item updated successfully')
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Item not found')
        }