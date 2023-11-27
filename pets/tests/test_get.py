import yaml
import pytest
from pets.helpers.json_helpers import JsonKeys
from pets.helpers.requestUtility import RequestUtility

with open("pets/helpers/values.yml", "r") as f:
    data = yaml.safe_load(f)
base_url = data['pending_url']

def test_status():
    raw = RequestUtility()
    statusCode = raw.get_status_code()
    assert statusCode == 200

def test_json_elements():
    jsonObject = JsonKeys()
    content = jsonObject.get_json_content(base_url)
    firstPeInfo = content[0]
    print(firstPeInfo)
    assert firstPeInfo['status'] == data['pending_status']

