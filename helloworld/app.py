from chalice import Chalice

app = Chalice(app_name="helloworld")


# @app.route("/")
# def index():
#     return {"hello": "world"}


app.debug = True


@app.on_sqs_message(queue="my-queue", batch_size=1)
def handle_sqs_message(event):
    for record in event:
        app.log.debug("Received message with contents: %s", record.body)
