import os
from coinspro_py import CoinsPro
from dotenv import load_dotenv

load_dotenv()
coinspro = CoinsPro()

coinspro.set_secret_key(os.getenv("SECRET_KEY"))
coinspro.set_api_key(os.getenv("API_KEY"))

coinspro.init()

##################### MARKET DATA ENDPOINTS #####################
# GET ORDERBOOK
# query = coinspro.market_data.get_orderbook(symbol="ETHPHP", limit=5)
# print(query)

# GET RECENT TRADES
# query = coinspro.market_data.get_recent_trade_list(symbol="ETHPHP", limit=2)
# print(query)

# KLINE/CANDLESTICK DATA
# Kline/Candlestick chart intervals:
# m -> minutes; h -> hours; d -> days; w -> weeks; M -> months
# 1m, 3m, 5m, 15m,30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
query = coinspro.market_data.get_candlestick_data(symbol="ETHPHP", interval="1h", limit=2)
print(query)

# CURRENT AVERAGE PRICE
# query = coinspro.market_data.get_current_average_price(symbol="ETHPHP")
# print(query)

# 24HR TICKER PRICE CHANGE STATISTICS
# query = coinspro.market_data.get_24hour_ticker_change_stat(symbol="ETHPHP")
# print(query)
# queryMany = coinspro.market_data.get_24hour_ticker_change_stat(symbols=["ETHPHP", "BTCUSDT"])
# print(queryMany)

# SYMBOL PRICE TICKER
# Latest price for a symbol or symbols.
# query = coinspro.market_data.get_symbol_price_ticker(symbol="ETHPHP")
# print(query)
# queryMany = coinspro.market_data.get_symbol_price_ticker(symbols=["ETHPHP", "BTCUSDT"])
# print(queryMany)

# SYMBOL ORDER BOOK TICKER
# Best price/qty on the order book for a symbol or symbols.
# query = coinspro.market_data.get_symbol_orderbook_ticker(symbol="ETHPHP")
# print(query)
# queryMany = coinspro.market_data.get_symbol_orderbook_ticker(symbols=["ETHPHP", "BTCUSDT"])
# print(queryMany)

# CRYPTOASSET TRADING PAIRS
# query = coinspro.market_data.get_crypto_assets_trading_pairs()
# print(query)