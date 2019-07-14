FROM python:3.7-alpine
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system
COPY src ./app/src/
COPY app.py test-aiohttp.py docker/entrypoint.sh ./app/
WORKDIR app/
ENTRYPOINT ["sh", "entrypoint.sh"]
