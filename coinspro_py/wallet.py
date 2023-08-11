import time
from coinspro_py.utils import _send_request, _create_signature

class Wallet:
    def __init__(self, secret_key, api_key, base_url):
        self.base_url = base_url
        self.secret_key = secret_key
        self.api_key = api_key

    def get_all_coins_info(self, recvWindow=None):
        params = {
            "timestamp": int(time.time() * 1000),
        }
        
        if recvWindow:
            params["recvWindow"] = recvWindow
        
        params["signature"] = _create_signature(params=params, secret_key=self.secret_key)

        return _send_request("GET", endpoint="/openapi/wallet/v1/config/getall", params=params, api_key=self.api_key, base_url=self.base_url)

    def get_deposit_address(self, coin, network, recvWindow=None):
        params = {
            "coin" : coin,
            "network": network,
            "timestamp": int(time.time() * 1000),
        }
        
        if recvWindow:
            params["recvWindow"] = recvWindow
        
        params["signature"] = _create_signature(params=params, secret_key=self.secret_key)

        return _send_request("GET", endpoint="/openapi/wallet/v1/deposit/address", params=params, api_key=self.api_key, base_url=self.base_url)

    def withdraw(self, coin, network, address, amount, addressTag=None, withdrawOrderId=None, recvWindow=None):
        params = {
            "coin" : coin,
            "network": network,
            "address": address,
            "amount": amount,
            "timestamp": int(time.time() * 1000),
        }
        
        if addressTag:
            params["addressTag"] = addressTag
        if withdrawOrderId:
            params["withdrawOrderId"] = withdrawOrderId
        if recvWindow:
            params["recvWindow"] = recvWindow
        
        params["signature"] = _create_signature(params=params, secret_key=self.secret_key)

        return _send_request("POST", endpoint="/openapi/wallet/v1/withdraw/apply", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def get_deposit_history(self, coin=None, txId=None, status=None, startTime=None, endTime=None, offset=None, limit=None, recvWindow=None):
        params = {
            "timestamp": int(time.time() * 1000),
        }
        
        if coin:
            params["coin"] = coin
        if txId:
            params["txId"] = txId
        if status:
            params["status"] = status
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit
        if recvWindow:
            params["recvWindow"] = recvWindow
        
        params["signature"] = _create_signature(params=params, secret_key=self.secret_key)

        return _send_request("GET", endpoint="/openapi/wallet/v1/deposit/history", params=params, api_key=self.api_key, base_url=self.base_url)

    def get_withdraw_history(self, coin=None, txId=None, status=None, startTime=None, endTime=None, offset=None, limit=None, recvWindow=None):
        params = {
            "timestamp": int(time.time() * 1000),
        }
        
        if coin:
            params["coin"] = coin
        if txId:
            params["txId"] = txId
        if status:
            params["status"] = status
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        if offset:
            params["offset"] = offset
        if limit:
            params["limit"] = limit
        if recvWindow:
            params["recvWindow"] = recvWindow
        
        params["signature"] = _create_signature(params=params, secret_key=self.secret_key)

        return _send_request("GET", endpoint="/openapi/wallet/v1/withdraw/history", params=params, api_key=self.api_key, base_url=self.base_url)

