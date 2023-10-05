import json


def handler(event, context):
    return json.dumps(event)
