import json
import time


def handler(event, context):
    start_time = time.time()
    print(json.dumps(event))
    end_time = time.time()
    processing_time = end_time - start_time
    min_wait_time = 1
    wait_time = max(0, min_wait_time - processing_time)
    time.sleep(wait_time)
