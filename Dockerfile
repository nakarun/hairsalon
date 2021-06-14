FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev

RUN pip install --upgrade pip
COPY ./requirements/base.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /var/run/hairsalon

CMD ["gunicorn", "config.wsgi", "--bind=unix:/var/run/hairsalon/hairsalon.sock"]