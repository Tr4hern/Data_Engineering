from detoxify import Detoxify
import json

from torch import det

def detoxify_analyse(text):

    results = Detoxify('original').predict(text)
    result = {}
    for i in results.keys():
        if(results[i] >= 0.5):
            result[i] = results[i]
    
    if bool(result) is False:
        result['Toxicity Detector'] = text + " is not toxic"

    return result


def detoxify_json_to_string(json_file):
    return json.dumps(str(json_file))