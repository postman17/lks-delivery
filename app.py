import json

from flask import Flask, request
from flask import Response

from src.parsers.pochta.street_to_postal_index import StreetToPostalIndex
from src.parsers.pochta.pochta import CostCalculation
from src.conf import (
    POST_API_RU_URL, POST_API_RU_APIKEY, POSTPRICE_RU_URL,
    POSTPRICE_RU_MASS, POSTPRICE_RU_VALUATION, POSTPRICE_RU_VAT)

app = Flask(__name__)


@app.route('/pochta')
def main():
    from_city = request.args.get('from_city')
    from_street = request.args.get('from_street')
    to_city = request.args.get('to_city')
    to_street = request.args.get('to_street')
    from_index = StreetToPostalIndex.get_index(POST_API_RU_URL, POST_API_RU_APIKEY, from_city, from_street)
    to_index = StreetToPostalIndex.get_index(POST_API_RU_URL, POST_API_RU_APIKEY, to_city, to_street)
    cost = CostCalculation.get_price(
        POSTPRICE_RU_URL, from_index, to_index, POSTPRICE_RU_MASS,
        POSTPRICE_RU_VALUATION, POSTPRICE_RU_VAT)
    data = {
        'pochta': cost
    }
    js = json.dumps(data)
    response = Response(js, status=200, mimetype='application/json')
    return response
# pochta?from_city=москва&from_street=алтуфьевское&to_city=уфа&to_street=парковая

@app.route('/echo')
def echo():
    data = {
        'Example': 'Echo Request'
    }
    js = json.dumps(data)
    response = Response(js, status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run()
