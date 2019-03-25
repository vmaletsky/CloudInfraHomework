# Readme

This repository contains a simple Python http server which responds to GET request with a Fibonacci number. 
The calculation is VERY inefficient, CPU and memory consuming. Also you can find the dockerfile to build a docker image and bash scripts for kubernetes deployment.

## Docker image

Docker image can be build from Dockerfile:

```bash
docker image build -t "vmaletsky/homeworkapp:v1" .
```

Or otherwise the image can be pulled from the docker hub:

```bash
docker pull vmaletsky/homeworkapp:v1
```

Start the http server:

```bash
docker run -d -p 81:81 vmaletsky/homeworkapp:v1
```

And start a calculation:

```bash
curl localhost:81
```

## Kubernetes

Create Kubernetes deployment and start a service:

```bash
bash deploy.sh
```

This simple bash script will start Minikube, create deployment and service using 
deployment.yaml and service.yaml files.

After the script has finished, we can check that our service and pod are running:

```bash
kubectl get all
```

Now, to start our calculation we need minikube ip and nodeport:
```bash
minikube ip

>192.168.99.100
```


```bash
kubectl get service kubernetes-homework

NAME                  TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes-homework   NodePort   10.101.187.167   <none>        81:32527/TCP   2m
```

The port that we need is 32527. Now we can make a request to our http server:

```bash
curl 192.168.99.100:32527
```

After we got the result, we can delete deployment and service using cleanup script:

```bash
bash cleanup.sh
```


### Deploy a local image

In the previous steps we used the docker image from docker hub. Now, 
if we want to use the local image:

```bash
bash deploy_local.sh
```

### Liveness and readiness probes

To create the liveness and readiness probes we need first to create deployment 
and start the service and then:

```bash
bash liveness.sh
```

It will create the liveness and readiness probes from liveness_readiness.yaml, sleep for 
5 seconds and show the status of the probe.

If we want to check its status at any time:

```bash
kubectl describe pod liveness-http
```
