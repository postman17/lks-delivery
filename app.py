import json

from flask import Flask, request
from flask import Response


app = Flask(__name__)


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
