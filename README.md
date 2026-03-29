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

📸 Screenshots:
<img width="1416" height="743" alt="Screenshot 2026-03-29 130724" src="https://github.com/user-attachments/assets/74a45c29-371a-4c83-a42c-e625a8aac461" />
<img width="1919" height="568" alt="Screenshot 2026-03-29 130652" src="https://github.com/user-attachments/assets/9dc4b3b4-809e-4254-b3b5-c1223429fad8" />
<img width="1919" height="796" alt="Screenshot 2026-03-29 130634" src="https://github.com/user-attachments/assets/66f7b320-37a7-4e8d-9559-5c9d550602b3" />
<img width="1919" height="805" alt="Screenshot 2026-03-29 130624" src="https://github.com/user-attachments/assets/f2852791-dc54-416d-b562-218f8b2ee273" />


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
