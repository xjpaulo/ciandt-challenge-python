FROM python:3-alpine

RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre

RUN mkdir -p /opt/app
RUN mkdir -p /scripts/python
ENV PROJECT_HOME /opt/app

COPY ./app $PROJECT_HOME

COPY requirements.txt $PROJECT_HOME
WORKDIR $PROJECT_HOME
RUN pip3 install -r requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 8080
CMD ["uwsgi", "--ini", "/opt/app/wsgi.ini"]
