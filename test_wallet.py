from coinspro_py import CoinsPro

coinspro = CoinsPro()

coinspro.set_secret_key("4wG4ERoeNOarBAgc4z68Au1nUlfghWbM2s4wUhKKSYTlIXyK2GvWPUxvOglwv24e")
coinspro.set_api_key("tkI87B4vIR9dhkDCm9zQi5qzpla9UmT9YmQTwH5XUcldYorCvagt6dRckP9FJpmq")

coinspro.init()

##################### WALLET ENDPOINTS #####################
# ALL COINS’ INFORMATION (USER_DATA)
# query = coinspro.wallet.get_all_coins_info()
# print(query)

# DEPOSIT ADDRESS (USER_DATA)
# Network can be found on coinspro.wallet.get_all_coins_info()
# on networklist array then select network field
# query = coinspro.wallet.get_deposit_address("AAVE", "ETH")
# print(query)
# query = coinspro.wallet.get_deposit_address("AAVE", "BSC")
# print(query)

# WITHDRAW(USER_DATA)
# Please notice coin/network/address/addressTag combination MUST be in withdraw address whitelist, it is needed to setup the withdraw address whitelist before doing this api call.
# not tested

# DEPOSIT HISTORY (USER_DATA)
# query = coinspro.wallet.get_deposit_history()
# print(query)

# WITHDRAWHISTORY (USER_DATA)
# query = coinspro.wallet.get_withdraw_history()
# print(query)