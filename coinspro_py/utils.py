import hashlib
import hmac
import requests
import urllib.parse

# Generate HMAC SHA256 signature, params as queryString, SECRECT KEY as key
def _create_signature(params, secret_key=""):
    # concat all params
    query_string = urllib.parse.urlencode(params)
    return hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def _send_request(method, endpoint, params=None, api_key="", base_url=""):
    url = base_url + endpoint
    headers = {
        "X-COINS-APIKEY": api_key
    }
    
    if method == "GET":
        response = requests.get(url, headers=headers, params=params)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=params)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers, data=params)
        
    if response.status_code == 200:
        return response.json()
    else:            
        print(f"Error: {response.status_code} - {str(response.json())}")
        return None