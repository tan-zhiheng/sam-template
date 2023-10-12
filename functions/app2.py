import requests
import json


def handler(event, context):
    url = "https://fakestoreapi.com/products"
    res = requests.get(url)
    return {
        "statusCode": res.status_code,
        "body": json.dumps(res.json()),
    }
