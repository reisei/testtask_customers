## Environment setup

Please, make sure that all bash scripts in `./scripts` directory are executable, if you're not sure, run 
```
chmod +x -R ./scripts
```

Let's run the minikube itself:
``` 
minikube start --insecure-registry 127.0.0.1
```
and then run script for setup minikube addons (ingress, registry) and socat for registry being available from host machine:
```
./script/setup.sh
```

This setup have been tested on Ubuntu 20.04 with docker driver (I guess it's the default one) for minikube 1.21.0

## Application build and deploy

First, build and test application with
```
./scripts/ci.sh
```

Then, deploy application to the minikube cluster:
```
./scripts/cd.sh
```

## Checking the endpoints

We can test the endpoints with curl:
```
curl -H 'Host: customer-a.local' http://$(minikube ip)/api/v1/hello
curl -H 'Host: customer-b.local' http://$(minikube ip)/api/v1/hello

```

## Cleaning up

Delete socat container with
```
./scripts/cleanup.sh
```
And delete minikube:
```
minikube delete
```
