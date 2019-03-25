#!/usr/bin/env bash
minikube start

eval $(minikube docker-env)

docker build -t vmaletsky/homeworkapp:v1 .

kubectl run kubernetes-homework --image=vmaletsky/homeworkapp:v1 --image-pull-policy=Never && kubectl expose deployment kubernetes-homework --port=81 --target-port=81 --type=NodePort
