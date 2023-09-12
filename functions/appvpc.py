from requests import get
import json


# aws lambda function handler
def handler(event, context):
    ip = get("https://api.ipify.org").content.decode("utf8")
    print("My public IP address is: {}".format(ip))
    body = {"public_ip": ip}
    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
