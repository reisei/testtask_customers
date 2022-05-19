FROM python:3.10.4
ENV FLASK_APP=helloworld

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt && \
    pip install -e .

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
