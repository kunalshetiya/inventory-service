# 🚀 Inventory Service - CI/CD & Monitoring Pipeline

A **production-ready FastAPI microservice** with end-to-end **CI/CD pipeline**, **Dockerization**, and **real-time monitoring using Prometheus & Grafana**.

---

## 📌 Features

- ⚡ FastAPI backend with REST APIs for inventory management  
- 📊 Custom **Prometheus metrics**:
  - Request count  
  - Request latency  
  - Error tracking  
  - Inventory updates  
- 🔄 **GitLab CI/CD Pipeline**:
  - Automated testing  
  - Docker image build  
- 🐳 Fully **Dockerized application**  
- 📈 **Monitoring Stack**:
  - Prometheus (metrics collection)  
  - Grafana (visual dashboards)  
- 🧠 Real-time observability using **Golden Signals**

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI  
- **DevOps:** Docker, Docker Compose  
- **CI/CD:** GitLab CI  
- **Monitoring:** Prometheus, Grafana  
- **Testing:** FastAPI TestClient  

---

## 🏗️ Architecture


Developer Push

      ↓
      
GitLab CI Pipeline

(Test Stage → Build Stage)

      ↓
Docker Image Built

      ↓
      
Application Runs via Docker Compose

      ↓
      
Prometheus scrapes /metrics

      ↓
      
Grafana Visualizes Metrics

📊 Monitoring (Golden Signals)

---

This project tracks key production metrics:

Latency → API response time

Traffic → Number of requests

Errors → Failed requests

Saturation → System resource usage

🚀 How to Run Locally
1. Clone the repository
git clone https://github.com/kunalshetiya/inventory-service.git
cd inventory-service

3. Run with Docker Compose
docker compose up -d
🌐 Access Services
FastAPI App: http://localhost:8000/health
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Username: admin
Password: admin
🧪 CI/CD Pipeline

Pipeline includes:

✅ Automated health check test
✅ Dependency installation
✅ Docker image build
✅ Runs on push to main branch
📸 Screenshots (Add Here)
GitLab Pipeline Success ✅
Grafana Dashboard 📊
Prometheus Targets 🎯
🔗 Project Links
🔧 GitLab (CI/CD):
https://gitlab.com/kunalshetiya-group/inventory-service
💻 GitHub:
https://github.com/kunalshetiya/inventory-service
💡 Why This Project Stands Out
Combines backend + DevOps + monitoring
Demonstrates real-world production practices
Shows end-to-end system design skills
Strong resume + interview project
⭐ Future Improvements
Kubernetes deployment
Auto-scaling
Alertmanager integration
Distributed tracing (Jaeger)
