import requests
import json

URL="http://127.0.0.1:8000/studapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data,)
    headers = {'content-type':'application/json'}
    r = requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'name':'Ravan',
        'roll':586,
        'city':'Nanded'
    }
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.post(url=URL,headers=headers, data=json_data)
    data=r.json()
    print(data)

def update_data():
    data = {
        'id':2,
        'roll':109,
        'name':'Templraory',
        'city':'Hyd'
    }
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.put(url=URL,headers=headers, data=json_data)
    data=r.json()
    print(data)

def delete_data():
    data = {'id':3}
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data=r.json()
    print(data)

delete_data()
#get_data()
#post_data()
#update_data()

