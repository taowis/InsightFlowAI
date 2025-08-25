from fastapi import FastAPI
from pydantic import BaseModel
import datetime as dt

app = FastAPI(title="ClientPulseAI API")

class Health(BaseModel):
    status: str
    timestamp: str

@app.get("/health", response_model=Health)
def health():
    return Health(status="ok", timestamp=dt.datetime.utcnow().isoformat())

@app.post("/reports/generate")
def generate_report():
    return {"ok": True, "message": "Report generation triggered (stub)"}

@app.post("/agents/run")
def run_agent():
    return {"ok": True, "message": "Agent workflow triggered (stub)"}
