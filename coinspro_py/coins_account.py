import time
import hashlib
import hmac
import requests
import urllib.parse

class CoinsAccount:
    def __init__(self):
        self.base_url = "https://api.pro.coins.ph"
    
    def set_secret_key(self, secret_key):
        self.secret_key = secret_key

    def set_api_key(self, api_key):        
        self.api_key = api_key

    # Generate HMAC SHA256 signature, params as queryString, SECRECT KEY as key
    def _create_signature(self, query_params):
        # concat all params
        query_string = urllib.parse.urlencode(query_params)
        return hmac.new(self.secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    def _send_request(self, method, endpoint, params=None):
        url = self.base_url + endpoint
        print(url)
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
            print(f"Error: {response.status_code} - {str(response.json())}")
            return None
            
    def get_account_info(self):
        params = {
            "recvWindow": 5000,  # Optional parameter, can be omitted if not needed
            "timestamp": int(time.time() * 1000),
        }
        
        params["signature"] = self._create_signature(params)

        return self._send_request("GET", endpoint="/openapi/v1/account", params=params)

    def new_order(self, symbol, side, orderType, time_in_force='GTC', quantity=None, quote_order_qty=None,
                  price=None, new_client_order_id=None, stop_price=None, new_order_resp_type=None,
                  stp_flag=None, recv_window=5000, quoteOrderQty=None):
        # Required params
        params = {
            'symbol': symbol,
            'side': side,
            'type': orderType,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if time_in_force:
            params["timeInForce"] = time_in_force
        if quoteOrderQty:
            params["quoteOrderQty"] = quoteOrderQty
        if quantity:
            params["quantity"] = quantity
        if quote_order_qty:
            params["quoteOrderQty"] = quote_order_qty
        if price:
            params["price"] = price
        if new_client_order_id:
            params["newClientOrderId"] = new_client_order_id
        if stop_price:
            params["stopPrice"] = stop_price
        if new_order_resp_type:
            params["newOrderRespType"] = new_order_resp_type
        if stp_flag:
            params["stpFlag"] = stp_flag
        if recv_window:
            params["recvWindow"] = recv_window
        
        params["signature"] =self._create_signature(params)
        return self._send_request("POST", endpoint="/openapi/v1/order/test", params=params)
