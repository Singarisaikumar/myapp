from fastapi import FastAPI
import os
import socket
import time

app = FastAPI(
    title="Production Platform API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "service": "production-platform-api",
        "status": "healthy",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "local")
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/ready")
def readiness():
    return {
        "status": "READY"
    }


@app.get("/api/orders")
def orders():
    time.sleep(0.1)

    return {
        "orders": [
            {
                "id": 1001,
                "status": "completed"
            },
            {
                "id": 1002,
                "status": "processing"
            }
        ]
    }