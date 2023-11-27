import yaml
import pytest
from pets.helpers.json_helpers import JsonKeys
from pets.helpers.requestUtility import RequestUtility
import requests

requestBody = {
  'id': 0,
  'petId': 0,
  'quantity': 20,
  'shipDate': '2023-11-22T07:25:06.141Z',
  'status': 'placed',
  'complete': True,
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

base_url = 'https://petstore.swagger.io/v2/store/order'
get_url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'
create_user = 'https://petstore.swagger.io/v2/user'
headers = {'content-type':'application/json', 'Accept':'application/json'}




def test_new_user():
    r = RequestUtility()
    raw_response = r.create_an_order(base_url, requestBody, headers=headers)
    quantity_placed = raw_response[1]
    orderDate = raw_response[2]
    orderStatus = raw_response[3]
    assert quantity_placed == 20
    assert orderDate == "2023-11-22T07:25:06.141+0000"
    assert orderStatus == 'placed'

def test_with_wrong_url():
    r = RequestUtility()
    raw_response = r.check_test_status(get_url, requestBody, headers=headers)
    assert raw_response == 405

def test_create_and_delete_new_user():
    r = RequestUtility()
    raw_response = r.create_new_user(create_user, dataForDeletion, headers=headers)
    user_name = "Peter"
    delete_user_name = requests.delete(create_user+user_name, json=dataForDeletion, headers=headers)
    import pdb; pdb.set_trace()



