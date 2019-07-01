

class CostCalculation(CustomParser):
	
    def _send_request(self, index_from, index_to):
        return requests.get(POSTPRICE_RU_URL.format(index_from, index_to, POSTPRICE_RU_MASS, POSTPRICE_RU_VALUATION, POSTPRICE_RU_VAT))

    def _parse_response(self, response):
        response = response.json()
        if response:
            return response['pkg']
        return

    @staticmethod
    def get_price(index_from, index_to):
        request = CostCalculation()._send_request(index_from, index_to)
        response = CostCalculation()._parse_response(request)
        return Response(response) if response else Response('not found')