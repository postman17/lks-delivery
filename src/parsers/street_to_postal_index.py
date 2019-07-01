


class StreetToPostalIndex(CustomParser):
    def _send_request(self, city, street):
        return requests.get(POST_API_RU_URL.format(city, street, POST_API_RU_APIKEY))

    def _parse_response(self, response):
        response = response.json()
        if not response['content']:
            return
        elif response['content'][0]['indexes'][0]:
            return response['content'][0]['indexes'][0]
        else:
            return response['content'][0]['indexes'][1]

    @staticmethod
    def get_index(city, street):
        request = StreetToPostalIndex()._send_request(city, street)
        response = StreetToPostalIndex()._parse_response(request)
        return response if response else 'not found'
