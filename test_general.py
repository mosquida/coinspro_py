import os
from coinspro_py import CoinsPro
from dotenv import load_dotenv

load_dotenv()
coinspro = CoinsPro()

coinspro.set_secret_key(os.getenv("SECRET_KEY"))
coinspro.set_api_key(os.getenv("API_KEY"))

coinspro.init()

##################### GNERAL ENDPOINTS #####################

# # TEST CONNECTIVITY
# query = coinspro.test_connectivity()
# print(query)

# CHECK SERVER TIME
query = coinspro.check_server_time()
print(query)

# # EXCHANGE INFORMATION
# query = coinspro.exchange_info()
# print(query)