import json
import requests

class JsonKeys(object):

    def __init__(self):
        pass

    def get_json_content(self, url):
        url = requests.get(url)
        bytesContent = url.content
        jsonContent = bytesContent.decode('utf8').replace("'", '"')
        convertedToJson = json.loads(jsonContent)


        return convertedToJson