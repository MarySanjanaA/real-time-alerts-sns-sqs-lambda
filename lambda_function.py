
import json

def lambda_handler(event, context):
    for record in event['Records']:
        message = record['body']
        print("Received message:", message)
        # Process the alert here, e.g., trigger SMS, email, log, or dashboard update
    return {
        'statusCode': 200,
        'body': json.dumps('Alerts processed')
    }
