from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from models import (
    LivePowerStatus,
    EnergyDataPoint,
    DeviceResponse,
    DeviceUpdate,
    BillingSummary,
    ChatRequest,
    ChatResponse
)
from mock_data import (
    MOCK_DASHBOARD_LIVE,
    MOCK_ANALYTICS_HISTORY,
    MOCK_DEVICES,
    MOCK_BILLING_SUMMARY
)

app = FastAPI(title="VoltStream API")

# Configure CORS for React frontend (default Vite port is 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/dashboard/live", response_model=LivePowerStatus)
def get_live_dashboard():
    return MOCK_DASHBOARD_LIVE

@app.get("/api/v1/analytics/history", response_model=List[EnergyDataPoint])
def get_analytics_history(period: str = Query("daily", regex="^(daily|weekly|monthly)$")):
    if period in MOCK_ANALYTICS_HISTORY:
        return MOCK_ANALYTICS_HISTORY[period]
    raise HTTPException(status_code=400, detail="Invalid period")

@app.get("/api/v1/devices", response_model=List[DeviceResponse])
def get_devices():
    return MOCK_DEVICES

@app.patch("/api/v1/devices/{device_id}", response_model=DeviceResponse)
def update_device(device_id: str, update_data: DeviceUpdate):
    for device in MOCK_DEVICES:
        if device.id == device_id:
            device.is_on = update_data.is_on
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.get("/api/v1/billing/summary", response_model=BillingSummary)
def get_billing_summary():
    return MOCK_BILLING_SUMMARY

# AI Stubs (Weeks 3 & 4)
@app.post("/api/v1/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    return ChatResponse(reply=f"Mock Chat Reply to: {request.message}")

@app.post("/api/v1/qa", response_model=ChatResponse)
def qa_endpoint(request: ChatRequest):
    return ChatResponse(reply=f"Mock QA Reply to: {request.message}")

@app.post("/api/v1/agent", response_model=ChatResponse)
def agent_endpoint(request: ChatRequest):
    return ChatResponse(reply=f"Mock Agent Reply to: {request.message}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
