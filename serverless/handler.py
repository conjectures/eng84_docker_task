import json
import boto3
import os
import base64

region_name = os.environ['REGION_NAME']
aws_access_key_id = os.environ['SECRET_KEY']
aws_secret_access_key = os.environ['SECRET_KEY']


def sendEmail(event, context):
    print(event)
    raw_data = base64.b64decode(event['body'])

    print("Raw Data:")
    print(raw_data)
    data = dict(item.split('=') for item in raw_data.decode("utf-8").split('&'))
    print("Data:")
    print(data)
    name = data['name']
    source = data['source']
    subject = data['subject']
    message = data['message']
    destination = data['destination']

    _message = "Message from: " + name + "\nEmail: " + source + "\nMessage content: " + message
    client = boto3.client('ses')
    response = client.send_email(
        Destination={
            'ToAddresses': [destination]
            },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': _message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source=source,
    )

    return _message + str(region_name)
