import json
import boto3
import os


region_name = os.environ['REGION_NAME']
aws_access_key_id = os.environ['SECRET_KEY']
aws_secret_access_key = os.environ['SECRET_KEY']
source = os.environ['SOURCE']
destination = os.environ['DESTINATION']


def sendEmail(event, context):
    # Get body from POST request
    data = json.loads(event['body'])

    # Collect data
    pusher = data.get('push_data').get('pusher')
    tag = data.get('push_data').get('tag')
    repo = data.get('repository').get('repo_name')
    image = data.get('repository').get('name')

    # Compose subject and messages
    subject = 'DockeHub update'
    _message = "Automated message from DockerHub:\nUser {} has pushed image {} version {} on repo {}".format(pusher, image, tag, repo)

    # Use boto3 client for email service
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
