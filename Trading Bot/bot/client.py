import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

TESTNET_URL = "https://testnet.binancefuture.com"


def get_client():

    client = Client(
        API_KEY,
        API_SECRET
    )

    # Connect to Futures Testnet
    client.FUTURES_URL = TESTNET_URL + "/fapi"

    return client