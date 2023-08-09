import time
from coinspro_py.utils import _send_request, _create_signature

class MarketData:
    def __init__(self, secret_key, api_key, base_url):
        self.base_url = base_url
        self.secret_key = secret_key
        self.api_key = api_key

    def get_orderbook(self, symbol, limit=None):
        # Required params
        params = {
            'symbol': symbol,
        }
        
        if limit:
            params["limit"] = limit
        
        return _send_request("GET", endpoint="/openapi/quote/v1/depth", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def get_recent_trade_list(self, symbol, limit=None):
        # Required params
        params = {
            'symbol': symbol,
        }
        
        if limit:
            params["limit"] = limit
        
        return _send_request("GET", endpoint="/openapi/quote/v1/trades", params=params, api_key=self.api_key, base_url=self.base_url)
    
    # Kline/Candlestick chart intervals:
    # m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
    # 1m, 3m, 5m, 15m,30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
    def get_candlestick_data(self, symbol, interval, startTime=None, endTime=None, limit=None):
        # Required params
        params = {
            'symbol': symbol,
            'interval': interval
        }
        
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        if limit:
            params["limit"] = limit
        
        return _send_request("GET", endpoint="/openapi/quote/v1/klines", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def get_current_average_price(self, symbol):
        params = {
            'symbol': symbol,
        }
        
        return _send_request("GET", endpoint="/openapi/quote/v1/avgPrice", params=params, api_key=self.api_key, base_url=self.base_url)
    
    def get_24hour_ticker_change_stat(self, symbol=None, symbols=None):
         # Required params
        params = {}
        
        if symbol:
            params["symbol"] = symbol
        if symbols:
            params["symbols"] = symbols
               
        return _send_request("GET", endpoint="/openapi/quote/v1/ticker/24hr", params=params, api_key=self.api_key, base_url=self.base_url)
    
    
    def get_symbol_price_ticker(self, symbol=None, symbols=None):
        # Required params
        params = {}
        
        if symbol:
            params["symbol"] = symbol
        if symbols:
            params["symbols"] = symbols
               
        return _send_request("GET", endpoint="/openapi/quote/v1/ticker/price", params=params, api_key=self.api_key, base_url=self.base_url)
    
    
    def get_symbol_orderbook_ticker(self, symbol=None, symbols=None):
        # Required params
        params = {}
        
        if symbol:
            params["symbol"] = symbol
        if symbols:
            params["symbols"] = symbols
               
        return _send_request("GET", endpoint="/openapi/quote/v1/ticker/bookTicker", params=params, api_key=self.api_key, base_url=self.base_url)
        
    
    def get_crypto_assets_trading_pairs(self):
       return _send_request("GET", endpoint="/openapi/v1/pairs", api_key=self.api_key, base_url=self.base_url)

