FROM python:3.9-slim

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
