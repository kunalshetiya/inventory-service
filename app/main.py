from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import time

# Import metrics
from app.metrics import (
    APP_INFO, REQUEST_COUNT, REQUEST_LATENCY, 
    STOCK_UPDATES, CURRENT_STOCK, ERROR_COUNT
)
from prometheus_client import make_asgi_app

app = FastAPI(title="Inventory Service")

# Set service info
APP_INFO.info({"version": "1.0.0", "environment": "production"})

class StockUpdate(BaseModel):
    product_id: str
    quantity: int
    action: str = "add"

stock_db = {"product1": 100, "product2": 50}

@app.get("/health")
async def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health", status="200").inc()
    return {"status": "healthy", "service": "inventory-service"}

@app.get("/stock/{product_id}")
async def get_stock(product_id: str):
    start_time = time.time()
    try:
        if product_id not in stock_db:
            raise HTTPException(status_code=404, detail="Product not found")
        
        quantity = stock_db[product_id]
        CURRENT_STOCK.labels(product_id=product_id).set(quantity)
        
        REQUEST_COUNT.labels(method="GET", endpoint="/stock", status="200").inc()
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(method="GET", endpoint="/stock").observe(latency)
        
        if random.random() < 0.2:
            time.sleep(0.3)
        
        return {"product_id": product_id, "stock": quantity}
    except Exception as e:
        ERROR_COUNT.labels(type=type(e).__name__).inc()
        raise

@app.post("/update-stock")
async def update_stock(update: StockUpdate):
    start_time = time.time()
    try:
        if update.product_id not in stock_db:
            raise HTTPException(status_code=404, detail="Product not found")
        
        if update.action == "add":
            stock_db[update.product_id] += update.quantity
        elif update.action == "remove":
            stock_db[update.product_id] = max(0, stock_db[update.product_id] - update.quantity)
        else:
            raise HTTPException(status_code=400, detail="Invalid action")
        
        CURRENT_STOCK.labels(product_id=update.product_id).set(stock_db[update.product_id])
        STOCK_UPDATES.labels(product_id=update.product_id, action=update.action).inc()
        
        REQUEST_COUNT.labels(method="POST", endpoint="/update-stock", status="200").inc()
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(method="POST", endpoint="/update-stock").observe(latency)
        
        return {"message": "Stock updated", "new_stock": stock_db[update.product_id]}
    except Exception as e:
        ERROR_COUNT.labels(type=type(e).__name__).inc()
        raise

# Prometheus metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
