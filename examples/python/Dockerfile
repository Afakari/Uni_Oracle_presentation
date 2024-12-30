FROM docker.arvancloud.ir/python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends  unzip wget libaio1 gcc python3-dev libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt
COPY ./setup_Instant_client.sh /tmp/setup_Instant_client.sh

RUN bash /tmp/setup_Instant_client.sh

COPY ./python_app .

CMD ["python", "main.py"]