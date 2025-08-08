.
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes
│   │   │   ├── __init__.py
│   │   │   ├── anomaly.py
│   │   │   └── login.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── anomaly.py
│   │   │   └── user.py
│   │   ├── db.py
│   │   ├── security.py
│   │   ├── config.py
│   │   └── utils.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic.ini
│   └── alembic
│       ├── env.py
│       ├── versions
│       │   └── <timestamp>_init_db.py
├── frontend
│   ├── public
│   │   ├── index.html
│   ├── src
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── components
│   │       ├── NavBar.jsx
│   │       ├── LoginForm.jsx
│   │       └── Dashboard.jsx
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   └── tailwind.config.js
├── k8s
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── docker-compose.yaml
├── README.md
└── .gitignore

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
passlib[bcrypt]
python-jose
alembic

import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

import React from "react";
import NavBar from "./components/NavBar";
import LoginForm from "./components/LoginForm";
import Dashboard from "./components/Dashboard";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/login" component={LoginForm} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/" component={Dashboard} />
      </Switch>
    </Router>
  );
}

export default App;

import React from "react";
import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav className="bg-blue-500 p-4">
      <div className="container mx-auto">
        <div className="flex items-center justify-between">
          <div className="text-white text-lg font-bold">Anomaly Detection</div>
          <div>
            <Link to="/dashboard" className="text-white mr-4">Dashboard</Link>
            <Link to="/login" className="text-white">Login</Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default NavBar;

import React, { useState } from "react";

function LoginForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    console.log(data);
  };

  return (
    <div className="container mx-auto mt-10">
      <div className="max-w-md mx-auto bg-white rounded-lg overflow-hidden md:max-w-md">
        <div className="md:flex">
          <div className="w-full">
            <form onSubmit={handleSubmit} className="p-4">
              <div className="mb-4">
                <label className="block text-grey-darker text-sm font-bold mb-2">Username</label>
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                  placeholder="Username"
                />
              </div>
              <div className="mb-4">
                <label className="block text-grey-darker text-sm font-bold mb-2">Password</label>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                  placeholder="Password"
                />
              </div>
              <div className="mb-4">
                <button
                  type="submit"
                  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                >
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoginForm;

import React, { useEffect, useState } from "react";

function Dashboard() {
  const [anomalies, setAnomalies] = useState([]);

  useEffect(() => {
    const fetchAnomalies = async () => {
      const response = await fetch("/api/anomalies");
      const data = await response.json();
      setAnomalies(data);
    };

    fetchAnomalies();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-xl font-bold mb-4">Anomalies</h1>
      <div className="bg-white shadow-md rounded-lg p-4">
        <ul>
          {anomalies.map((anomaly) => (
            <li key={anomaly.id}>
              {anomaly.detected_at} - {anomaly.description} - {anomaly.status}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Dashboard;

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Anomaly Detection</title>
    <link href="/dist/output.css" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>

FROM node:14-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "start"]

{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^5.2.0",
    "tailwindcss": "^2.2.19"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}

module.exports = {
  purge: [],
  darkMode: false,
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

version: "3.8"

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=anomaly
      - POSTGRES_SERVER=postgres
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: anomaly
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: backend:latest
        ports:
        - containerPort: 8000
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: frontend:latest
        ports:
        - containerPort: 3000

apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  selector:
    app: backend
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000

apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: anomaly-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: anomaly.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 3000
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 8000

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