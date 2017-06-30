FROM nginx:latest

MAINTAINER Jonas Einarsson <docker@jonaseinarsson.se>

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
