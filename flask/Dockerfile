FROM python:3.9.1-alpine

WORKDIR /app

ADD . /app

RUN apk add --no-cache gcc libc-dev linux-headers; pip install -r requirements.txt --no-cache-dir

CMD ["uwsgi", "app.ini"]