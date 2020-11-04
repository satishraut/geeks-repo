import requests
import json
URL="http://127.0.0.1:8000/create/"

data={
    'name':'Ramesh',
    'roll':102,
    'city':'Pune'
}

json_data = json.dumps(data)
r = requests.post(URL, data=json_data)
data = r.json()
print(data['msg'])