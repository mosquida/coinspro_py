from coinspro_py.coins_account import Account
from coinspro_py.utils import _send_request, _create_signature

class CoinsPro:
    def __init__(self):
        self.base_url = "https://api.pro.coins.ph"

    def set_secret_key(self, secret_key):
        self.secret_key = secret_key

    def set_api_key(self, api_key):        
        self.api_key = api_key
        
    def init(self):
        self.account = Account(secret_key=self.secret_key, api_key=self.api_key, base_url=self.base_url)
        
        
    # GENERAL ENDPOINTS
    def test_connectivity(self):
        return _send_request("GET", endpoint="/openapi/v1/ping", api_key=self.api_key, base_url=self.base_url)
    
    def check_server_time(self):
        return _send_request("GET", endpoint="/openapi/v1/time", api_key=self.api_key, base_url=self.base_url)
    
    def exchange_info(self):
        return _send_request("GET", endpoint="/openapi/v1/exchangeInfo", api_key=self.api_key, base_url=self.base_url)
