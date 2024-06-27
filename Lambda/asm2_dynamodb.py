import boto3


class Reminder:

    def __init__(self):
        client = boto3.resource('dynamodb')
        self.table = client.Table('asm2-ccp302x')

    def  Create_data(self , event):
        expiryTimestamp = int(time.time() + 5)
        response = self.table.put_item(
            Item={
                'id': event['id'],
                'user_email': event['name'],
                'TTL': expiryTimestamp,
                'message': event['message']
            }
        )
        return {
            'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
            'body': 'Record ' + event['id'] + ' added'
        }    

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
                ':m':event['message']
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
        if event['tasktype']  == "create":
            create_result =  pet_Object.Create_data(event['data'])
            return create_result
        elif event['tasktype']  == "read":
            read_result =  pet_Object.Read_data(event['data'])
            return read_result
        elif event['tasktype']  == "update":
            update_result =  pet_Object.Update_data(event['data'])
            return update_result
        elif event['tasktype']  == "delete":
            delete_result =  pet_Object.Delete_data(event['data'])
            return delete_result
        else :
            return {
                'statusCode': '404',
                'body': 'Not found'
            }