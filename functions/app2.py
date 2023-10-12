import requests
import json
from jinja2 import Environment, FileSystemLoader


def handler(event, context):
    # url = "https://fakestoreapi.com/products"
    # res = requests.get(url)

    env = Environment(
        loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True
    )

    template = env.get_template("apigateway+lambda.yaml")
    result = template.render(json.loads(event.body))
    return {
        "statusCode": 200,
        "body": json.dumps({"template": result}),
    }
