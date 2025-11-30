# DevOps Final Project

This repository contains a full-stack DevOps project with:

* A **Frontend** application deployed on **Kubernetes using YAML**
* A **Flask Backend** application run via **Docker CLI commands**

This project demonstrates:

* Docker image creation and usage
* Kubernetes Deployments & Services
* NodePort networking
* Manual container execution

---

## 📁 Folder Structure

```
DEVOPS_FINAL_PROJECT/
│
├── flask/                  # Backend Flask application
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/               # Frontend application
│   ├── dist/                # Production build output
│   ├── src/                 # Frontend source code
│   ├── public/              # Public static assets
│   ├── nginx.conf           # NGINX configuration
│   ├── node.yaml            # Kubernetes Deployment & Service
│   ├── Dockerfile           # Frontend Docker image
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

### Folder Purpose

* **flask/** → Contains the backend API and its Docker configuration
* **frontend/** → Contains the frontend app, Dockerfile, and Kubernetes YAML
* **frontend/node.yaml** → Controls frontend Deployment & Service in Kubernetes

---

## Flask Backend Deployment Using kubectl (CLI Driven)

The Flask backend is deployed using **Docker + Kubernetes CLI commands** instead of a YAML file.

---

### Step 1: Navigate to Flask Directory

```bash
cd flask
```

---

### Step 2: Build the Docker Image

```bash
docker build -t flask-app .
```

Builds the Flask backend image locally.

---

### Step 3: Tag the Image for Docker Hub

```bash
docker tag flask-app uojha/flask-app:latest
```

Prepares the image for upload to Docker Hub.

---

### Step 4: Push the Image to Docker Hub

```bash
docker push uojha/flask-app:latest
```

Makes the backend image publicly available for Kubernetes to pull.

---

### Step 5: Create Backend Deployment

```bash
kubectl create deployment backend --image=uojha/flask-app:latest
```

Creates a Kubernetes Deployment that manages the Flask backend container.

---

### Step 6: Scale the Backend Deployment

```bash
kubectl scale deployment backend --replicas=3
```

Runs **3 Flask backend pods** for load balancing and high availability.

---

### Step 7: Verify Backend Pods

```bash
kubectl get pods
kubectl get pods --show-labels
```

Confirms that all Flask pods are running.

---

### Step 8: Expose Backend via NodePort Service

```bash
kubectl expose deployment backend \
  --type=NodePort \
  --port=5000 \
  --target-port=8888
```

Exposes the Flask backend to external traffic.

---

### Step 9: Access Flask Backend

```bash
minikube service backend --url
```

Returns a public URL such as:

```
http://127.0.0.1:62761
```

---
## Frontend Deployment Using Kubernetes (YAML)

The frontend is deployed using Kubernetes via the `node.yaml` file.

### Step 1: Make Sure Kubernetes Is Running

If using Minikube:

```bash
minikube start
```

This starts a local Kubernetes cluster.

---

### Step 2: Apply the Kubernetes YAML

```bash
kubectl apply -f frontend/node.yaml
```

---

### Step 3: Verify Deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

You should see:

* 4 frontend pods running
* One NodePort service

---

### Step 4: Access the Frontend in Browser

```bash
minikube service frontend-service
```

This opens the frontend in your browser.

---

## Core Technologies Used

* Docker
* Kubernetes
* NGINX
* Flask (Python)
* Vite / Node.js frontend
* Minikube


## Notes

* The frontend uses a **NodePort Service** for browser access
* The backend is currently not exposed inside Kubernetes
* Both systems are running independently


## Author

Utsav Ojha
uojha@clarku.edu

