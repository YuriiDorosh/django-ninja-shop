FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap

ADD pyproject.toml /app

RUN pip install --upgrade pip

COPY . /app/
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN chmod +x /entrypoint.sh
