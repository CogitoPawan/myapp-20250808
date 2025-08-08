# Anomaly Detection System

This is a microservices-based Anomaly Detection System with a FastAPI backend and ReactJS frontend.

## Prerequisites

- Docker
- Docker Compose
- Kubernetes (minikube or similar for local testing)

## Setup

### Running with Docker Compose

1. Navigate to the project directory.
2. Run `docker-compose up --build`
3. Access the frontend at `http://localhost:3000`

### Running with Kubernetes

1. Navigate to the `k8s` directory.
2. Run `kubectl apply -f deployment.yaml`
3. Run `kubectl apply -f service.yaml`
4. Run `kubectl apply -f ingress.yaml`
5. Ensure your ingress controller is configured correctly.
6. Access the system at `http://anomaly.example.com`

## Backend API Documentation

After running the backend, Swagger documentation can be accessed at `http://localhost:8000/docs`