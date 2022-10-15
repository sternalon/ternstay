# -*- coding: utf-8 -*-

""" Tests for ternstay.stipe_functions """

from datetime import date

from ternstay import stripe_functions


class TestStripeFunctions:
    def test_set_api_key(self):
        stripe = stripe_functions.set_api_key("AAAA")
        assert stripe.api_key == "AAAA"

    def test_parse_balace_response_as_listy(self):

        balanace_obj = {
            "available": [
                {"currency": "gbp", "amount": 1},
                {"currency": "eur", "amount": 2},
            ],
            "pending": [
                {"currency": "gbp", "amount": 4},
                {"currency": "eur", "amount": 5},
            ],
        }
        current_date = date.fromisoformat("2019-12-04")
        balance_list = stripe_functions.parse_balace_response_as_list(
            balanace_obj, current_date
        )

        expected = [
            {
                "date": current_date,
                "currency": "gbp",
                "available_amount": 1,
                "pending_amount": 4,
            },
            {
                "date": current_date,
                "currency": "eur",
                "available_amount": 2,
                "pending_amount": 5,
            },
        ]

        assert balance_list == expected
