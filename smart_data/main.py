from tinydb import TinyDB
import requests
db = TinyDB('db.json',indent=4)
tiem = db.table('Vivo')
def get_brend():
    return  tiem.all()

def send_data():
    url = "http://127.0.0.1:8000/field/add/"
    for item in get_brend():
        r = requests.post(url,json=item)
        print(r.status_code)
    return "OK"

print(send_data())

























# import json 
# import requests
# import time
# def send_data(data):
#     url = "http://127.0.0.1:8000/field/add/"
#     r = requests.post(url,json=data)
#     return r.status_code

# with open("db.json",'r') as file:
#     data = json.load(file)

# apple = data['Redmi']

# for i, v in apple.items():
#     s = ''
#     mom = ''
#     for j in v["RAM"]:
#         if j.isdigit():
#             print(v["RAM"],j)
#             s+=j
#         else:
#             break
#     for j in v['memory']:
#         if j.isdigit():
#             print(v["memory"],j)
#             mom+=j
#         else:
#             break
#     item = {
#         "price":(v['price']),
#         "img_url":v["img_url"],
#         "color":v["color"],
#         "ram":int(s),
#         "memory":int(mom),
#         "name":v["name"],
#         "model":v["company"]
#     }
#     print(send_data(item))
#     time.sleep(2)
