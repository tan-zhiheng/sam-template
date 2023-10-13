from jinja2 import Environment, FileSystemLoader
import json

env = Environment(
    loader=FileSystemLoader("functions/templates"), trim_blocks=True, lstrip_blocks=True
)

template = env.get_template("apigateway+lambda.yaml")

with open("test.json") as f:
    d = json.load(f)

print(d)

result = template.render(d)

with open("test-output.yaml", "w") as f:
    f.write(result)
