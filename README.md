# Inventory Service

A production-like Python FastAPI microservice for e-commerce inventory management with built-in Prometheus observability.

## Features
- REST APIs: `/health`, `/stock/{product_id}`, `/update-stock`
- Custom Prometheus metrics (Golden Signals + business metrics)
- Dockerized for consistent deployment
- Ready for GitLab CI/CD and Prometheus + Grafana monitoring

## Endpoints
- Health: `GET /health`
- Get stock: `GET /stock/product1`
- Update stock: `POST /update-stock`
- **Metrics**: `GET /metrics/` (Prometheus format)

## Run locally with Docker
```bash
docker build -t inventory-service:latest .
docker run -p 8000:8000 inventory-service:latest
Project Structure

app/main.py - FastAPI application with custom metrics
app/metrics.py - Prometheus metric definitions
Dockerfile - Production-ready container
requirements.txt - Python dependencies

This service is designed to be monitored with Prometheus + Grafana and deployed via GitLab CI.
