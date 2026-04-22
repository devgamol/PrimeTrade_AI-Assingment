"""Simple CLI for collecting order input parameters."""

import argparse
import json

try:
    from bot.logging_config import get_logger
except ModuleNotFoundError:
    from logging_config import get_logger


def main() -> None:
    """Parse CLI arguments, log them, and print formatted JSON."""
    parser = argparse.ArgumentParser(description="Simple trading bot CLI")
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--side", type=str, required=True)
    parser.add_argument("--type", type=str, required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float, required=False)

    args = parser.parse_args()

    symbol = args.symbol
    side = args.side
    order_type = args.type
    qty = args.qty
    price = args.price

    logger = get_logger(__name__)
    logger.info(
        "Received CLI params: symbol=%s side=%s type=%s qty=%s price=%s",
        symbol,
        side,
        order_type,
        qty,
        price,
    )

    parsed_args = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "qty": qty,
        "price": price,
    }
    print(json.dumps(parsed_args, indent=2))


if __name__ == "__main__":
    main()
