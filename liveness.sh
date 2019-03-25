#!/usr/bin/env bash
kubectl create -f liveness_readiness.yaml

sleep 5

kubectl describe pod liveness-http