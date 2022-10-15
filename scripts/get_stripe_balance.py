import datetime
import logging
import sys

import requests

from ternstay import stripe_functions

LOGGER = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_stripe_balance():
    date = datetime.datetime.now()
    balance_obj = stripe_functions.get_balance()
    balances = stripe_functions.parse_balace_response_as_list(balance_obj, date)

    for item in balances:
        print(item)


if __name__ == "__main__":
    try:
        LOGGER.info("Running Stripe balance import")
        get_stripe_balance()

    except Exception as exc:
        LOGGER.info("Stripe balance import failed")

        raise exc
