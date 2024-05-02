FROM python:3.9-bullseye

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc musl-dev libpq-dev postgresql && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt && \
    rm -rf /root/.cache

COPY . /app

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000"]
