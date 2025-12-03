# dockerize_node_app_assignment

A sample Node.js application prepared for Docker and Kubernetes exercises. This repository demonstrates how to containerize a Node app, run it with Docker, orchestrate with Docker Compose, and deploy to Kubernetes (minikube/kind/remote cluster).

---

## Table of Contents

- Project Overview
- Prerequisites
- Project Structure
- Quick Start
    - Local (Node)
    - Docker (build & run)
    - Docker Compose
    - Kubernetes (minikube/kind/remote)
- Configuration & Environment
- Dockerfile (example)
- docker-compose.yml (example)
- Kubernetes Manifests (examples)
    - Deployment
    - Service
    - ConfigMap / Secret (optional)
- Test & Debug
- Common Commands
- Troubleshooting
- Notes & Next Steps
- License

---

## Project Overview

This project contains a minimal Node.js HTTP server designed for teaching how to:
- Create a production-ready Docker image.
- Use docker-compose for local multi-container setups.
- Deploy to Kubernetes with simple manifests.
- Configure environment variables and health checks.

The app exposes an HTTP endpoint (default: GET /) that returns a JSON status.

---

## Prerequisites

- Node.js (for local dev): v14+
- npm or yarn
- Docker Desktop (or Docker Engine)
- docker-compose (v1.27+ or Docker Compose v2)
- kubectl
- minikube or kind (for local Kubernetes) or access to a remote Kubernetes cluster
- (Optional) Docker Hub (or another container registry) account to push images

---

## Project Structure

Assumed repository layout:

- README.md
- package.json
- src/
    - index.js
- Dockerfile
- docker-compose.yml
- k8s/
    - deployment.yaml
    - service.yaml
    - configmap.yaml (optional)
    - secret.yaml (optional)
- .dockerignore
- .env.example

Adjust names/paths to match your actual files.

---

## Quick Start

### 1) Local (Node)
Install and run locally:
```bash
npm install
npm start
# or
node src/index.js
```
Visit: http://localhost:3000

### 2) Docker: build & run
Build the image (tag as you like):
```bash
docker build -t mynodeapp:latest .
```
Run container:
```bash
docker run --rm -p 3000:3000 --env-file .env example_mynodeapp mynodeapp:latest
```
Verify:
```bash
curl http://localhost:3000/
```

Push to registry:
```bash
docker tag mynodeapp:latest <registry>/<username>/mynodeapp:latest
docker push <registry>/<username>/mynodeapp:latest
```

### 3) Docker Compose
Start app (and dependent services if any):
```bash
docker-compose up --build
```
Stop:
```bash
docker-compose down
```

### 4) Kubernetes (minikube/kind/remote)
Using local minikube:
```bash
# ensure image is available to the cluster (minikube)
minikube image build -t mynodeapp:latest .

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# check
kubectl get pods,svc
kubectl port-forward svc/mynodeapp 3000:3000
# then visit http://localhost:3000
```
If pushing to a remote registry, update the image in deployment.yaml to the registry path.

---

## Configuration & Environment

Use environment variables for config. Provide .env.example:

.env.example
```
PORT=3000
NODE_ENV=production
APP_MESSAGE="Hello from Dockerized Node app"
```

In Kubernetes, prefer ConfigMap for non-sensitive and Secret for sensitive values.

---

## Dockerfile (example)

Dockerfile (multi-stage recommended)
```dockerfile
# Stage 1: build
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .

# Stage 2: runtime
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app . 
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "src/index.js"]
```

Use .dockerignore to exclude node_modules, logs, .git, etc.

---

## docker-compose.yml (example)

```yaml
version: "3.8"
services:
    app:
        build: .
        image: mynodeapp:local
        ports:
            - "3000:3000"
        env_file:
            - .env
        restart: unless-stopped
```

Add other services (db, redis) as needed.

---

## Kubernetes Manifests (examples)

k8s/deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: mynodeapp
spec:
    replicas: 2
    selector:
        matchLabels:
            app: mynodeapp
    template:
        metadata:
            labels:
                app: mynodeapp
        spec:
            containers:
                - name: mynodeapp
                    image: <registry>/<user>/mynodeapp:latest
                    ports:
                        - containerPort: 3000
                    envFrom:
                        - configMapRef:
                                name: mynodeapp-config
```

k8s/service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
    name: mynodeapp
spec:
    type: ClusterIP
    selector:
        app: mynodeapp
    ports:
        - port: 3000
            targetPort: 3000
            protocol: TCP
```

Add readiness/liveness probes to production manifests.

---

## Test & Debug

- Logs:
    - Docker: docker logs <container>
    - Kubernetes: kubectl logs <pod>
- Exec into container:
    - docker exec -it <container> /bin/sh
    - kubectl exec -it <pod> -- /bin/sh
- Port-forwarding for local inspection:
    - kubectl port-forward svc/mynodeapp 3000:3000

Add unit/integration tests with Jest/Mocha and include in CI.

---

## Common Commands Cheat Sheet

- Build image: docker build -t mynodeapp:latest .
- Run container: docker run --rm -p 3000:3000 mynodeapp:latest
- Compose up: docker-compose up --build
- List images: docker images
- Push image: docker push <repo>/mynodeapp:latest
- Apply k8s manifests: kubectl apply -f k8s/
- Delete k8s resources: kubectl delete -f k8s/

---

## Troubleshooting

- App not reachable:
    - Check container logs and app binding to 0.0.0.0
    - Ensure port mapping is correct
- Image not found in k8s:
    - Push image to registry or use minikube image load / kind load docker-image
- Permission issues:
    - Use compatible base image, adjust file ownership if mounting host volumes

---

## Notes & Next Steps

- Add CI pipeline to build and push images (GitHub Actions, GitLab CI).
- Add automated tests and vulnerability scanning.
- Harden images by using smaller base images and non-root users.
- Add Helm chart for templated Kubernetes deployment.

---

## License

FREE

---

