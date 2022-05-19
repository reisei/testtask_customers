docker build . -t localhost:5000/helloworld:1.0.0 && \
docker run --rm -it localhost:5000/helloworld:1.0.0 sh -c 'FLASK_CLIENTNAME=CustomerA pytest' && \
docker push localhost:5000/helloworld:1.0.0

