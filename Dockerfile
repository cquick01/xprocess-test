FROM python:3-buster

RUN apt-get update && \
    apt-get -y full-upgrade && \
    apt-get -y install python3-pip

RUN pip install pytest pytest-cov pytest-xprocess pipenv

COPY . /opt

WORKDIR /opt

RUN pipenv sync
