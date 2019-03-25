#!/usr/bin/env bash
kubectl delete service kubernetes-homework && kubectl delete deployment kubernetes-homework && kubectl delete pod liveness-http