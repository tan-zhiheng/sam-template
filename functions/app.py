import json


def handler(event, context):
    return {
        "statusCode": 200,
        "event": json.dumps(event),
    }
