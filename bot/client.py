"""Binance Futures client with real and mock support."""

import random

class BinanceClient:
    def __init__(self, api_key: str, api_secret: str, use_mock: bool = False) -> None:
        self.use_mock = use_mock
        self.client = None
        if not self.use_mock:
            try:
                from binance.client import Client
            except ModuleNotFoundError as exc:
                raise ModuleNotFoundError(
                    "python-binance is not installed. Install it with: pip install python-binance"
                ) from exc
            self.client = Client(api_key, api_secret, testnet=True)
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET" if order_type == "MARKET" else "LIMIT",
            "quantity": quantity,
        }

        if params["type"] == "LIMIT":
            if price is None:
                raise ValueError("price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = "GTC"

        if self.use_mock:
            return {
                "orderId": random.randint(100000, 999999),
                "status": "FILLED",
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "executedQty": quantity,
            }

        try:
            return self.client.futures_create_order(**params)
        except Exception as exc:
            raise Exception(f"Failed to place Binance Futures order: {exc}") from exc
