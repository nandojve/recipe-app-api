FROM debian:buster
MAINTAINER Peregrine Consultoria e Serviços LTDA

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN apt update

# build-dep: dependencies
RUN apt install -y apt-utils gcc python3-dev

# postgis dependencies
RUN apt install -y libgeos-dev libproj-dev gdal-bin

# cryptography dependends + build-dep
RUN apt install -y libffi-dev libssl-dev

# psycopg2 dependencies + build-dep
RUN apt install -y libpq-dev postgresql-client

# pillow dependencies
RUN apt install -y libjpeg-dev zlib1g-dev

RUN apt install -y python3-pip

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

COPY ./requirements-dev.txt /requirements-dev.txt
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN useradd -ms /bin/bash user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
