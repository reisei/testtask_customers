minikube addons enable registry 
minikube addons enable ingress 
docker run -d --rm -it --name registry-socat --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
