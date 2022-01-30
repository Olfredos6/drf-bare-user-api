FROM python:3.10-slim
WORKDIR /app
COPY ./requirements.txt .
RUN apt update && \
    apt upgrade -y && \
    pip install --upgrade pip && pip install -r requirements.txt
COPY . .
