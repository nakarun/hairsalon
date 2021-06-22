FROM python:3.8.0-alpine

WORKDIR /usr/src/hairsalon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache gcc python3-dev musl-dev jpeg-dev zlib-dev

ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1
RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo

RUN pip install --upgrade pip
COPY ./requirements/base.txt /usr/src/hairsalon/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /var/run/hairsalon

CMD ["gunicorn", "config.wsgi", "--bind=unix:/var/run/hairsalon/hairsalon.sock"]