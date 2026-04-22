"""Order execution logic."""

try:
    from bot.validators import (
        validate_order_type,
        validate_price,
        validate_quantity,
        validate_side,
        validate_symbol,
    )
except ModuleNotFoundError:
    from validators import (
        validate_order_type,
        validate_price,
        validate_quantity,
        validate_side,
        validate_symbol,
    )


def execute_order(client, params: dict):
    try:
        validate_symbol(params.get("symbol"))
        validate_side(params.get("side"))
        validate_order_type(params.get("order_type"))
        validate_quantity(params.get("quantity"))
        validate_price(params.get("price"), params.get("order_type"))
    except Exception as exc:
        return {"success": False, "error": str(exc)}

    max_retries = 2
    attempts = 0

    while attempts <= max_retries:
        try:
            response = client.place_order(
                symbol=params.get("symbol"),
                side=params.get("side"),
                order_type=params.get("order_type"),
                quantity=params.get("quantity"),
                price=params.get("price"),
                stop_price=params.get("stop_price"),
            )
            return {
                "success": True,
                "data": {
                    "symbol": str(response.get("symbol")),
                    "status": str(response.get("status")),
                    "orderId": int(response.get("orderId")),
                    "executedQty": float(response.get("executedQty")),
                },
            }
        except Exception as exc:
            attempts += 1
            if attempts > max_retries:
                return {"success": False, "error": str(exc)}
