#!/bin/bash

set -x

echo "Start gunicorn"

gunicorn -b 0.0.0.0:5442 app:app --worker-class aiohttp.GunicornWebWorker --access-logfile /access.log --error-logfile /error.log --log-level "warning"

