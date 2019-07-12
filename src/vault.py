import requests


def get_apikey():
    headers = {"X-Vault-Token": "s.zvXg5hWRRTM9QH8CBMcrXH8V"}
    r = requests.get('http://vault:8200/v1/secret/postapi-apikey', headers=headers)
    json_response = r.json()
    if json_response.get('data'):
        return json_response.get('data')['apikey']
