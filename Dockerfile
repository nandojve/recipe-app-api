FROM python:3.7-alpine
MAINTAINER Peregrine Consultoria e Serviços LTDA

ENV PYTHONUNBUFFERED 1

# build-dep: dependencies
RUN apk add gcc musl-dev python3-dev

# cryptography dependends + build-dep
RUN apk add libffi-dev openssl-dev

# psycopg2 dependencies + build-dep
RUN apk add postgresql-dev

# pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev

COPY ./requirements-dev.txt /requirements-dev.txt
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
