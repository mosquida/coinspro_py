import time
import hashlib
import hmac
import requests

class CoinsAccount:
    def __init__(self):
        self.base_url = "https://api.pro.coins.ph"
    
    def set_secret_key(self, secret_key):
        self.secret_key = secret_key

    def set_api_key(self, api_key):        
        self.api_key = api_key

    def _create_signature(self, query_params):
        query_string = '&'.join([f"{key}={query_params[key]}" for key in sorted(query_params.keys())])
        signature = hmac.new(self.secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        return signature
    
    def _send_request(self, method, endpoint, params=None, data=None):
        url = self.base_url + endpoint
        headers = {
            "X-COINS-APIKEY": self.api_key
        }
        
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, )
        elif method == "POST":
            response = requests.post(url, data=params, headers=headers)
            
        if response.status_code == 200:
            return response.json()
        else:            
            print(f"Error: {response.status_code} - {response.json()['msg']}")
            return None
            
    def get_account_info(self):
        # Set the required parameters for the request
        params = {
            "recvWindow": 5000,  # Optional parameter, can be omitted if not needed
            "timestamp": int(time.time() * 1000),
        }

        params["signature"] = self._create_signature(params)

        # response = requests.get(f"{self.base_url}/openapi/v1/account", headers=headers, params=params)
        response = self._send_request("GET", endpoint="/openapi/v1/account", params=params)
        return response
