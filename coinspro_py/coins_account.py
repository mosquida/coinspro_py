import time
from coinspro_py.utils import _send_request, _create_signature

class Account:
    def __init__(self, secret_key, api_key, base_url):
        self.base_url = base_url
        self.secret_key = secret_key
        self.api_key = api_key

            
    def get_account_info(self):
        params = {
            "recvWindow": 5000,  # Optional parameter, can be omitted if not needed
            "timestamp": int(time.time() * 1000),
        }
        
        params["signature"] = _create_signature(params=params, secret_key=self.secret_key)

        return _send_request("GET", endpoint="/openapi/v1/account", params=params, api_key=self.api_key, base_url=self.base_url)

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
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v1/order", params=params, api_key=self.api_key, base_url=self.base_url)

    def test_new_order(self, symbol, side, orderType, time_in_force='GTC', quantity=None, quote_order_qty=None,
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
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v1/order/test", params=params, api_key=self.api_key, base_url=self.base_url)

    # Parameter orderId or origClientOrderId is required.
    def query_order(self, orderId=None, origClientOrderId=None, recv_window=5000):
        # Required params
        params = {
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if orderId:
            params["orderId"] = orderId
        if origClientOrderId:
            params["origClientOrderId"] = origClientOrderId
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/order", params=params, api_key=self.api_key, base_url=self.base_url)

    # Parameter orderId or origClientOrderId is required.
    def cancel_order(self, orderId=None, origClientOrderId=None, recv_window=5000):
        # Required params
        params = {
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if orderId:
            params["orderId"] = orderId
        if origClientOrderId:
            params["origClientOrderId"] = origClientOrderId
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("DELETE", endpoint="/openapi/v1/order", params=params, api_key=self.api_key, base_url=self.base_url)
 
    def cancel_all_open_orders(self, symbol, recv_window=5000):
        # Required params
        params = {
            'symbol': symbol,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("DELETE", endpoint="/openapi/v1/openOrders", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def query_all_open_orders(self, symbol="", recv_window=5000):
     # Required params
        params = {
            'symbol': symbol,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/openOrders", params=params, api_key=self.api_key, base_url=self.base_url)
    
    
    def get_history_orders(self, symbol="", orderId=None, startTime=None, endTime=None, limit=None, recv_window=5000):
     # Required params
        params = {
            'symbol': symbol,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if orderId:
            params["orderId"] = orderId
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime  
        if limit:
            params["limit"] = limit    
            
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/historyOrders", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def get_account_trade_list(self, symbol, orderId=None, fromId=None, startTime=None, endTime=None, limit=None, recv_window=5000):
        # Required params
        params = {
            'symbol': symbol,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if orderId:
            params["orderId"] = orderId
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime  
        if fromId:
            params["fromId"] = fromId  
        if limit:
            params["limit"] = limit    
            
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/myTrades", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def withdraw_to_coinsph_account(self, coin, amount, withdrawOrderId=None, recv_window=5000):
        # Required params
        params = {
            'coin': coin,
            'amount': amount,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if withdrawOrderId:
            params["withdrawOrderId"] = withdrawOrderId
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v1/capital/withdraw/apply", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def deposit_to_exchange_account(self, coin, amount, depositOrderId=None, recv_window=5000):
        # Required params
        params = {
            'coin': coin,
            'amount': amount,
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if depositOrderId:
            params["depositOrderId"] = depositOrderId
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v1/capital/deposit/apply", params=params, api_key=self.api_key, base_url=self.base_url)
    
    # DEPOSIT ORDER WHICH DEPOSIT COINS_PH TO EXCHANGE history 
    def get_deposit_order_history(self, coin=None, depositOrderId=None, status=None, offset=None, limit=None, startTime=None, endTime=None, recv_window=5000):
        # Required params
        params = {
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if coin:
            params["coin"] = coin
        if depositOrderId:
            params["depositOrderId"] = depositOrderId
        if status:
            params["status"] = status
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit    
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
            
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/capital/deposit/history", params=params, api_key=self.api_key, base_url=self.base_url)

    # WITHDRAWAL ORDER WHICH WITHDRAW FROM EXCHANGE TO COINS_PH history
    def get_withdraw_order_history(self, coin=None, depositOrderId=None, status=None, offset=None, limit=None, startTime=None, endTime=None, recv_window=5000):
        # Required params
        params = {
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if coin:
            params["coin"] = coin
        if depositOrderId:
            params["depositOrderId"] = depositOrderId
        if status:
            params["status"] = status
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit    
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
            
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/capital/withdraw/history", params=params, api_key=self.api_key, base_url=self.base_url)

    def get_trade_fee(self, symbol=None, recv_window=5000):
         # Required params
        params = {
            'recvWindow': recv_window,
            'timestamp': int(time.time() * 1000),
        }
        
        if symbol:
            params["symbol"] = symbol
                   
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v1/asset/tradeFee", params=params, api_key=self.api_key, base_url=self.base_url)
        
    
    def payment_request(self, payer_contact_info, receiving_account, amount, message, supported_payment_collectors=None, expires_at=None):
         # Required params
        params = {
            'payer_contact_info': payer_contact_info,
            'receiving_account': receiving_account,
            'amount':amount,
            'message': message,
            'timestamp': int(time.time() * 1000),
        }
        
        if supported_payment_collectors:
            params["supported_payment_collectors"] = supported_payment_collectors
        if expires_at:
            params["expires_at"] = expires_at
                   
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v3/payment-request/payment-requests", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def get_payment_request(self, id, start_time=None, end_time=None, limit=None):
          # Required params
        params = {
            'id': id,
            'timestamp': int(time.time() * 1000),
        }
        
        if start_time:
            params["start_time"] = start_time
        if end_time:
            params["end_time"] = end_time
        if limit:
            params["limit"] = limit
                   
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("GET", endpoint="/openapi/v3/payment-request/get-payment-request", params=params, api_key=self.api_key, base_url=self.base_url)
    

    def cancel_payment_request(self, id):
         # Required params
        params = {
            'id': id,
            'timestamp': int(time.time() * 1000),
        }
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v3/payment-request/delete-payment-request", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def send_payment_request_reminder(self, id):
        params = {
            'id': id,
            'timestamp': int(time.time() * 1000),
        }
        
        params["signature"] =_create_signature(params, secret_key=self.secret_key)
        return _send_request("POST", endpoint="/openapi/v3/payment-request/payment-request-reminder", params=params, api_key=self.api_key, base_url=self.base_url)
    
    