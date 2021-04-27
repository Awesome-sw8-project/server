FROM python:3.9.0-slim-buster

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN pip install --upgrade pip

COPY requirements.txt ./
COPY ./ ./
RUN pip install -r requirements.txt

EXPOSE 52200
ENTRYPOINT [ "python", "server.py" ]
