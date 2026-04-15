import argparse
import logging

from bot.logging_config import setup_logging

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.orders import (
    place_market_order,
    place_limit_order
)


def main():

    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(
            args.side
        )

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        price = validate_price(
            args.price,
            order_type
        )

        print("\nORDER SUMMARY")

        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if price:
            print("Price:", price)

        if order_type == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\nORDER RESPONSE")

        print(
            "Order ID:",
            response.get("orderId")
        )

        print(
            "Status:",
            response.get("status")
        )

        print(
            "Executed Qty:",
            response.get("executedQty")
        )

        if "avgPrice" in response:

            print(
                "Avg Price:",
                response.get("avgPrice")
            )

        print("\nSUCCESS")

    except Exception as e:

        logging.error(str(e))

        print(
            "\nFAILED:",
            str(e)
        )


if __name__ == "__main__":
    main()