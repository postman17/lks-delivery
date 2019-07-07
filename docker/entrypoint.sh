#!/bin/bash

set -x

echo "Start gunicorn"

gunicorn -b 0.0.0.0:5442 app:app --worker-class aiohttp.GunicornWebWorker

echo "End"
