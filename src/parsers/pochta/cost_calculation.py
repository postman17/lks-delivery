from .base_parser import BaseParser


class CostCalculation(BaseParser):
    def parse(self, response):
        response = response.json()
        if response:
            return response.get('pkg')
        return

    @staticmethod
    def output(attrs: dict) -> dict:
        request = CostCalculation().send_request(attrs)
        response = CostCalculation().parse(request)
        return {
            'pochta': response
        }
