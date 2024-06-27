import boto3


class Reminder:

    def __init__(self):
        client = boto3.resource('dynamodb')
        self.table = client.Table('asm2-ccp302x')


    def  Read_data(self , event):
        response = self.table.get_item(
            Key={
                'id': event['id']
            }
        )
        if 'Item' in response:
            return response['Item']
        else:
            return {
                'statusCode': '404',
                'body': 'Not found'
            }

    def  Update_data(self , event):
        response = self.table.update_item(
            Key={'id': event['id']},
            ExpressionAttributeNames={
                '#E': 'user_email',
                '#M': 'message'
            },
            ExpressionAttributeValues={
                ':e': event['user_email'],
                ':m': event['message']
            },
            UpdateExpression='SET #E = :e, #M = :m',
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'body': 'Record ' + event['id'] + ' updated'
        }

    def  Delete_data(self , event):
        response = self.table.delete_item(
            Key={
                'id': event['id']
            }
        )

        return {
                'statusCode': '200',
                'body': 'Deleted the item with id :' + event['id']
            }

def lambda_handler(event, context):
    if event:
        asm2_reminder =  Reminder()
        if event['tasktype']  == "read":
            read_result =  asm2_reminder.Read_data(event['data'])
            return read_result
        elif event['tasktype']  == "update":
            update_result =  asm2_reminder.Update_data(event['data'])
            return update_result
        else :
            return {
                'statusCode': '404',
                'body': 'Not found'
            }