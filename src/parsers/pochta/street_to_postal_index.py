from .base_parser import BaseParser


class StreetToPostalIndex(BaseParser):
    def parse(self, response):
        response = response.json()
        if not response['content']:
            return
        elif response['content'][0]['indexes'][0]:
            return response['content'][0]['indexes'][0]
        else:
            return response['content'][0]['indexes'][1]

    @staticmethod
    def output(attrs: dict, city: str, street: str) -> int:
        attrs['city'] = city
        attrs['street'] = street
        request = StreetToPostalIndex().send_request(attrs)
        response = StreetToPostalIndex().parse(request)
        return response
