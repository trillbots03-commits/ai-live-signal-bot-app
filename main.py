from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Signal Master 5.0", version="5.0.0")
app.include_router(router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "signal-master"}
