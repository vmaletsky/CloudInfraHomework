#!/usr/bin/env bash
#Start minikube
minikube start

#Create deployment and service
kubectl create -f deployment.yaml && kubectl create -f service.yaml
