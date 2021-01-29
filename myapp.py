import requests
import json

# URL = "http://www.omdbapi.com/?t=3+idiots&apikey=d6ac37d4"
# URL = "http://www.omdbapi.com/?i=Guardians of the Galaxy Vol. 2&apikey=d6ac37d4"
URL = "http://127.0.0.1:8000/api/movie/"


def getdata(title=None):
    data = {}
    if id is not None:
        data = {'title': title}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


getdata('Kesari')


# def getdata(title=None):
#     data = {}
#     if id is not None:
#         data = {'title': title}
#     json_data = json.dumps(data)
#     headers = {'content-Type': 'application/json'}
#     r = requests.get(url=URL, headers=headers, data=json_data)
#     data = r.json()
#     print(data)


# getdata()
