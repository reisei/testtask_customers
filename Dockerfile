FROM python:3.10.4
ENV FLASK_APP=helloworld

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt && \
    pip install -e .
