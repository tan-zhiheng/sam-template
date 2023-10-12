import requests
import json


def handler(event, context):
    # url = "https://fakestoreapi.com/products"
    # res = requests.get(url)

    return {
        "statusCode": 200,
        "body": json.dumps({"event": event}),
    }
