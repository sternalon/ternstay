import stripe

from ternstay import settings


def set_api_key(api_key=None):
    """Set the API key for the Stipe sdk. 
    If no api_key is provided, then the API key from settings is used.

        :param str api_key:
            API key to use

        :returns object stripe:
            Returns the stripe sdk object
     """
    if api_key:
        stripe.api_key = api_key
    else:
        stripe.api_key = settings.STRIPE_API_KEY
    return stripe


def get_balance():
    """Retrievs the balance from stripe using the Stripe SDK 
        :returns dict response:
            Returns the response object received from Strip
     """
    stripe = set_api_key()
    response = stripe.Balance.retrieve()
    return response


def parse_balace_response_as_list(balance_obj, date):
    """Reformats the balance object returned by the stripe API as a list of balances for each account

        :param dict balance_obj:
            The balance object returned by the stripe.balance API

        :param datatime date:
            Date at which balance was collected 

        :returns list balance_list:
            Returns a list containing the balances for each currency account
     """
    number_of_accounts = len(balance_obj["available"])
    balance_list = []

    for k in range(number_of_accounts):
        available = balance_obj["available"][k]
        pending = balance_obj["pending"][k]
        account_balance = {
            "date": date,
            "currency": available["currency"],
            "available_amount": available["amount"],
            "pending_amount": pending["amount"],
        }
        balance_list.append(account_balance)

    return balance_list
