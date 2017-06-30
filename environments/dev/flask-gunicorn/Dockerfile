FROM python:3.6.1
MAINTAINER Jonas Einarsson <docker@jonaseinarsson.se>

RUN apt-get update

ADD project/requirements /requirements

RUN pip install -r requirements/dev.txt

EXPOSE 8000

WORKDIR /src
