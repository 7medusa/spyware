#  written by medusa


import requests


def upload(name, data, ipadress, port=80):
    url = f"http://{ipadress}:{port}"
    data = {name:f'{data}'}
    response = requests.get(url, params=data)
    #print(response.url)
