import requests


class BaseParser:
    def send_request(self, attrs):
        return requests.get(attrs['url'].format(**attrs))
