# --- Base Python ---
FROM python:3.7-alpine AS base

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps \
                                ca-certificates \
                                gcc \
                                linux-headers \
                                musl-dev \
                                libffi-dev \
                                jpeg-dev zlib-dev \
                                bash

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install -r ./requirements.txt

RUN chmod +x /code/bin/run.sh

ENTRYPOINT [ "/code/bin/run.sh" ]