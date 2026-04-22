"""Simple validation helpers for CLI inputs."""


def validate_symbol(symbol: str) -> bool:
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("symbol must be a non-empty string")
    return True


def validate_side(side: str) -> bool:
    if side not in ("BUY", "SELL"):
        raise ValueError('side must be "BUY" or "SELL"')
    return True


def validate_order_type(order_type: str) -> bool:
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError('order_type must be "MARKET" or "LIMIT"')
    return True


def validate_quantity(qty: float) -> bool:
    if qty <= 0:
        raise ValueError("quantity must be greater than 0")
    return True


def validate_price(price: float, order_type: str) -> bool:
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("price is required and must be greater than 0 for LIMIT orders")
    return True
