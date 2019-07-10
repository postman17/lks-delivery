import requests


def get_apikey():
    headers = {"X-Vault-Token": "s.zvXg5hWRRTM9QH8CBMcrXH8V"}
    r = requests.get('http://127.0.0.1:8200/v1/secret/postapi-apikey', headers=headers)
    json_response = r.json()
    return json_response.get('data')['apikey']


print(get_apikey())