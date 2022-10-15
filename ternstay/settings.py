# -*- coding: utf-8 -*-

import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(dotenv_path=find_dotenv())


STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "not set")
