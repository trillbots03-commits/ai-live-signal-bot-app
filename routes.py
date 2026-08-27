from fastapi import APIRouter
from app.core.pipeline import analyze_market

router = APIRouter()


@router.get("/markets")
def markets() -> dict:
    return {"markets": ["EUR/USD", "BTC/USD", "NAS100"]}


@router.get("/markets/{symbol}/analysis")
def analysis(symbol: str) -> dict:
    return analyze_market(symbol)


@router.get("/markets/{symbol}/state")
def state(symbol: str) -> dict:
    return analyze_market(symbol)


@router.websocket("/ws/markets")
async def market_socket(websocket):
    await websocket.accept()
    await websocket.send_json({"event": "status", "state": "BLOCKED", "reason": "No live provider configured"})
    await websocket.close()
