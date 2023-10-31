FROM python:3.10.13-alpine3.17

COPY requirements.txt /temp/requirements.txt
COPY test /test
WORKDIR /test
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password test-user

USER test-user
