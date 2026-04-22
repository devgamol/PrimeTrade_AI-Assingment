"""CLI entrypoint to validate and execute orders."""

import argparse
import json

try:
    from bot.client import BinanceClient
    from bot.logging_config import get_logger
    from bot.orders import execute_order
    from bot.validators import (
        validate_order_type,
        validate_price,
        validate_quantity,
        validate_side,
        validate_symbol,
    )
except ModuleNotFoundError:
    from client import BinanceClient
    from logging_config import get_logger
    from orders import execute_order
    from validators import (
        validate_order_type,
        validate_price,
        validate_quantity,
        validate_side,
        validate_symbol,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple trading bot CLI")
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--side", type=str, required=True)
    parser.add_argument("--type", type=str, required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float, required=False)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    logger = get_logger(__name__)
    symbol = args.symbol
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.qty
    price = args.price

    params = {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
    }
    logger.info("Input params: %s", params)

    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)
        if args.dry_run:
            result = {
                "success": True,
                "data": {
                    "symbol": symbol,
                    "status": "DRY_RUN",
                    "orderId": 0,
                    "executedQty": float(quantity),
                },
            }
        else:
            client = BinanceClient("", "", use_mock=True)
            result = execute_order(client, params)
        logger.info("Order result: %s", result)
        print(json.dumps(result, indent=2))
    except Exception as exc:
        error_result = {"success": False, "error": str(exc)}
        logger.error("Order error: %s", error_result)
        print(json.dumps(error_result, indent=2))


if __name__ == "__main__":
    main()
