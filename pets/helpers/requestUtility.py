import json
import requests
import yaml
from pets.helpers.json_helpers import JsonKeys

baseUrl = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"
storeUrl = "https://petstore.swagger.io/v2/store/order"

with open("pets/helpers/values.yml", "r") as f:
    data = yaml.safe_load(f)
base_url = data['pending_url']

requestBody = {
  'id': 0,
  'petId': 0,
  'quantity': 0,
  'shipDate': '2023-11-22T07:25:06.141Z',
  'status': 'delivered',
  'complete': True
}

dataForDeletion = {
  "id": 0,
  "username": "Petr",
  "firstName": "Petr",
  "lastName": "Wong",
  "email": "no_email@.net",
  "password": "123",
  "phone": "2223322",
  "userStatus": 0
}

headers = {'content-type':'application/json', 'Accept':'application/json'}


class RequestUtility(object):

    def __init__(self):
        self.url = baseUrl


    def create_an_order(self, url, data, headers):
        create_new_order = requests.post(url, json=data, headers=headers)
        rs = create_new_order.content
        raw_body = rs.decode('utf8').replace("'", '"')
        order_id = json.loads(raw_body)['id']
        quantity = json.loads(raw_body)['quantity']
        order_ship_date = json.loads(raw_body)['shipDate']
        order_status = json.loads(raw_body)['status']
        return order_id, quantity, order_ship_date, order_status

    def check_test_status(self, url, data, headers):
        order_status = requests.post(url, json=data, headers=headers)
        return order_status.status_code

    def get_status_code(self):
        main_url = self.url
        raw_url = requests.get(main_url)
        return raw_url.status_code

    def create_new_user(self, url, data, headers):
        create_new_user = requests.post(url, json=data, headers=headers)
        rs = create_new_user.content
        raw_body = rs.decode('utf8').replace("'", '"')
        # name = json.loads(raw_body)['username']
        import pdb; pdb.set_trace()

