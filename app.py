import json

from flask import Flask, request
from flask import Response

from src.parsers.pochta.main import MailParser

app = Flask(__name__)


@app.route('/pochta')
def main():
    from_city = request.args.get('from_city')
    from_street = request.args.get('from_street')
    to_city = request.args.get('to_city')
    to_street = request.args.get('to_street')
    cost = MailParser.get_price(from_city, from_street, to_city, to_street)
    data = {
        'pochta': cost}
    js = json.dumps(data)
    response = Response(js, status=200, mimetype='application/json')
    return response
# pochta?from_city=москва&from_street=алтуфьевское&to_city=уфа&to_street=парковая


@app.route('/echo')
def echo():
    data = {
        'Example': 'Echo Request'}
    js = json.dumps(data)
    response = Response(js, status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run()
