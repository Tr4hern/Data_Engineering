import pandas as pd
from detoxify import Detoxify
import json

def detoxify_analyse(text):

    results = Detoxify('multilingual').predict(text)

    return results


def detoxify_json_to_string(json_file):
    return json.dumps(str(json_file))

