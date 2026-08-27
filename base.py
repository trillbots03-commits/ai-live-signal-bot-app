from abc import ABC, abstractmethod
from typing import Any


class MarketDataProvider(ABC):
    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def authenticate(self) -> None: ...

    @abstractmethod
    async def subscribe(self, symbols: list[str], timeframes: list[str]) -> None: ...

    @abstractmethod
    async def unsubscribe(self, symbols: list[str]) -> None: ...

    @abstractmethod
    async def get_historical_candles(self, symbol: str, timeframe: str, limit: int) -> list[dict[str, Any]]: ...

    @abstractmethod
    async def get_latest_price(self, symbol: str) -> dict[str, Any]: ...

    @abstractmethod
    async def get_ticks(self, symbol: str, limit: int) -> list[dict[str, Any]]: ...

    @abstractmethod
    async def get_status(self) -> str: ...

    @abstractmethod
    async def disconnect(self) -> None: ...
