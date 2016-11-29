FROM python:2.7-slim

WORKDIR /root/app
COPY requirements.txt /root/app
RUN pip install -r requirements.txt
