import requests
import json

URL="http://127.0.0.1:8000/studapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data,)
    r = requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'name':'Rajesh',
        'roll':99,
        'city':'Telgoan'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data=r.json()
    print(data)

def update_data():
    data = {
        'id':205,
        'name':'Ram',
        'city':'Telstra'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data=r.json()
    print(data)

def delete_data():
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data=r.json()
    print(data)

delete_data()
#get_data(1)
#post_data()
#update_data()

