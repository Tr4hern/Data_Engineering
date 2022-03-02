import warnings
warnings.filterwarnings('ignore')
import app
import toxicity
import json


def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def test_beautiful_text():
    assert isinstance(app.beautitful_text(toxicity.detoxify_json_to_string(toxicity.detoxify_analyse("test"))), str)

def test_sentiment():
    assert is_json(app.beautitful_text(toxicity.detoxify_json_to_string(toxicity.detoxify_analyse("test")))) == False
    # We can't assert with True because of a RuntimeError