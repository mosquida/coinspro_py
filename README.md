# coinspro-py

## Python library wrapper for Coins Pro REST API (https://coins-docs.github.io/rest-api/) 

Merchant Endpoint and Websockets Streams still in development !!!


Must setup the API first on your coinspro account
https://support.coins.ph/hc/en-us/articles/11620395767193-How-to-set-up-API-via-Coins-Pro

Set 1 public address of your computer
Keep the secret key and api key



```js
// must have python3 and poetry(https://python-poetry.org/docs/)
// install dependencies
poetry install

// activate the virtual environment
poetry shell

//create .env file on root folder and your keys
SECRET_KEY = "abc"
API_KEY = "xyz"

// run sample 
// uncomment sample code blocks to run
python3 test_general.py
python3 test_account.py
python3 test_market.py
python3 test_wallet.py
```


