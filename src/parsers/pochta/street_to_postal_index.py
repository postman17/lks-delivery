import requests

# from ...base import BaseParser


class StreetToPostalIndex:
    def _send_request(self, url, api_key, city, street):
        return requests.get(url.format(city, street, api_key))

    def _parse_response(self, response):
        response = response.json()
        if not response['content']:
            return
        elif response['content'][0]['indexes'][0]:
            return response['content'][0]['indexes'][0]
        else:
            return response['content'][0]['indexes'][1]

    @staticmethod
    def get_index(url, api_key, city, street):
        request = StreetToPostalIndex()._send_request(url, api_key, city, street)
        response = StreetToPostalIndex()._parse_response(request)
        return response if response else 'not found'
