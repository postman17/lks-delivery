import requests


class CostCalculation:
    def _send_request(self, url: str, index_from: int, index_to: int, mass: int, val: int, vat: int):
        return requests.get(url.format(index_from, index_to, mass, val, vat))

    def _parse_response(self, response):
        response = response.json()
        if response:
            return response['pkg']
        return

    @staticmethod
    def get_price(url: str, index_from: int, index_to: int, mass: int, val: int, vat: int) -> float:
        request = CostCalculation()._send_request(url, index_from, index_to, mass, val, vat)
        response = CostCalculation()._parse_response(request)
        return response
