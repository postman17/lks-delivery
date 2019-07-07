FROM python:3.7-alpine
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system
COPY src /src
ADD app.py /
ADD docker/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]

