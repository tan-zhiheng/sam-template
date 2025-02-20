import json

def lambda_handler(event, context):
    """Sample Lambda function for API Gateway integration"""

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda!",
            "event": event,
        }),
    }