
import json
import requests


def getdata(title=None):

    if title is not None:
        data = title
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url="http://www.omdbapi.com/?t="+data+"&apikey=d6ac37d4",
                     headers=headers, data=json_data)
    data = r.json()
    return data
