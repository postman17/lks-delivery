FROM python:3.7-alpine
WORKDIR /
COPY Pipfile Pipfile.lock docker/entrypoint.sh ./
RUN pip install pipenv && pipenv install --system
COPY src ./app/src/
COPY app.py test-aiohttp.py ./app/
ENTRYPOINT ["sh", "/entrypoint.sh"]
