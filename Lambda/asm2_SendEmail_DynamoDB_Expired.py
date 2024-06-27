import json
import boto3

def lambda_handler(event, context):
    print(event)
    if event['Records'][0]['eventName'] == "REMOVE":
        email = event['Records'][0]['dynamodb']['OldImage']['user_email']['S']
        message = event['Records'][0]['dynamodb']['OldImage']['message']['S']
        client = boto3.client("ses")
        subject = "Reminder For You"
        body = f'''You have 1 reminder: {message}'''
        message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
        response = client.send_email(Source = "thangfoseca@gmail.com",
                   Destination = {"ToAddresses": [email]}, Message = message)
        return response