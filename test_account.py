import os
from coinspro_py import CoinsPro
from dotenv import load_dotenv

load_dotenv()
coinspro = CoinsPro()

coinspro.set_secret_key(os.getenv("SECRET_KEY"))
coinspro.set_api_key(os.getenv("API_KEY"))

coinspro.init()

##################### ACCOUNT ENDPOINTS #####################
# ACCOUNT INFO
account_info = coinspro.account.get_account_info()
print(account_info)

# NEW ORDER
# CREATE SELL LIMIT ORDER(100pesos)
# response = coinspro.account.new_order(
#     symbol='ETHPHP',
#     side='SELL',
#     orderType='LIMIT',
#     quantity=0.001,
#     price=104000,
# )
# print(response)

# NEW TEST ORDER
# CREATE ORDER BUT NOTS SEND TO MACTHING ENGINE
# response = coinspro.account.new_order(
#     symbol='ETHPHP',
#     side='SELL',
#     orderType='LIMIT',
#     quantity=0.001,
#     price=104000,
# )
# print(response)

# QUERY SPECIFIC ORDER
# Parameter orderId or origClientOrderId is required.
# query = coinspro.account.query_order(orderId=1482574428487311360)
# print(query)

# CANCEL SPECIFIC ORDER
# Parameter orderId or origClientOrderId is required.
# query = coinspro.account.cancel_order(orderId=1479737531528404992)
# print(query)

# CANCEL All OPEN ORDERS ON A SYMBOL
# Parameter symbol is required.
# query = coinspro.account.cancel_all_open_orders(symbol="ETHPHP")
# print(query)

# QUERY All OPEN ORDER
# without symbol, gets all
# query = coinspro.account.query_all_open_orders()
# print(query)
# query = coinspro.account.query_all_open_orders(symbol="ETHPHP")
# print(query)

# GET HISTORY ORDER
# without symbol, gets all
# query = coinspro.account.get_history_orders()
# print(query)
# query = coinspro.account.get_history_orders(symbol="ETHPHP")
# print(query)

# GET ACCOUNT TRADE LIST
# query = coinspro.account.get_account_trade_list(symbol="ETHPHP")
# print(query)

# NOT TESTED
# deposit_to_exchange_account()
# withdraw_to_coinsph_account()

# DEPOSIT ORDER WHICH DEPOSIT COINS_PH TO EXCHANGE HISTORY
# query = coinspro.account.get_deposit_order_history()
# print(query)

# WITHDRAWAL ORDER WHICH WITHDRAW FROM EXCHANGE TO COINS_PH) (USER_DATA)
# query = coinspro.account.get_withdraw_order_history()
# print(query)

# GET TRADE FEE
# without symbol, gets all
# query = coinspro.account.get_trade_fee()
# print(query)
# query = coinspro.account.get_trade_fee(symbol="ETHPHP")
# print(query)