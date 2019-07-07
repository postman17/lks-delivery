import requests

from .base_parser import BaseParser


class CostCalculation(BaseParser):
    # def send_request(self, url: str, index_from: int, index_to: int, mass: int, val: int, vat: int):
    #     return requests.get(url.format(index_from, index_to, mass, val, vat))

    def parse(self, response):
        response = response.json()
        if response:
            return response.get('pkg')
        return

    @staticmethod
    def output(attrs: dict, index_from: int, index_to: int) -> dict:
        attrs['index_from'] = index_from
        attrs['index_to'] = index_to
        request = CostCalculation().send_request(attrs)
        response = CostCalculation().parse(request)
        return {
            'pochta': response
        }
