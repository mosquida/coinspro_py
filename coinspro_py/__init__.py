from coinspro_py.account import Account
from coinspro_py.market_data import MarketData
from coinspro_py.wallet import Wallet
from coinspro_py.websocket import WebSocket

from coinspro_py.utils import _send_request, _create_signature

class CoinsPro:
    def __init__(self):
        self.base_url = "https://api.pro.coins.ph"
        self.websocket = WebSocket()

    def set_secret_key(self, secret_key):
        self.secret_key = secret_key

    def set_api_key(self, api_key):        
        self.api_key = api_key
        
    def init(self):
        self.account = Account(secret_key=self.secret_key, api_key=self.api_key, base_url=self.base_url)
        self.market_data = MarketData(secret_key=self.secret_key, api_key=self.api_key, base_url=self.base_url)
        self.wallet = Wallet(secret_key=self.secret_key, api_key=self.api_key, base_url=self.base_url)
        
    # GENERAL ENDPOINTS
    def test_connectivity(self):
        return _send_request("GET", endpoint="/openapi/v1/ping", api_key=self.api_key, base_url=self.base_url)
    
    def check_server_time(self):
        return _send_request("GET", endpoint="/openapi/v1/time", api_key=self.api_key, base_url=self.base_url)
    
    def exchange_info(self):
        return _send_request("GET", endpoint="/openapi/v1/exchangeInfo", api_key=self.api_key, base_url=self.base_url)
