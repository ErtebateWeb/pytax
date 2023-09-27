import requests
import time

# Get the current timestamp (seconds since epoch)
timestamp_ms = int(time.time() * 1000)

print(f"Current timestamp: {timestamp_ms}")

timestamp = str(timestamp_ms)
headers_dict = {
  'requestTraceId': timestamp,
  'timestamp': timestamp,
  'Content-Type': 'application/json'  
}

print("headers-dict:",headers_dict)

headers_json = f'{{"requestTraceId": {headers_dict["requestTraceId"]}, "timestamp": {headers_dict["timestamp"]}, "Content-Type": "{headers_dict["Content-Type"]}"}}'

print("headers_json:",headers_json)

# Define the URL
url = 'https://tp.tax.gov.ir/req/api/tsp/sync/GET_TOKEN'

# Define the headers
headers = headers_json
# {
#     'requestTraceId': '1655185848687',
#     'timestamp': '1655185848687',
#     'Content-Type': 'application/json'
# }

# Define the request payload as a dictionary
payload = {
    'time': 1,
    'packet': {
        'uid': None,
        'packetType': 'GET_TOKEN',
        'retry': False,
        'data': {
            'username': 'test-tsp-id-1'
        },
        'encryptionKeyId': '',
        'symmetricKey': '',
        'iv': '',
        'fiscalId': '',
        'dataSignature': ''
    },
    'signature': 'IiIdkclswu3Krc8ZM7MQvEy7ZWzJmBPSl1CQrI0dhLGdRPRrmomVo+UkbdzRyuth9G4EnbgOjnjz5WJcfO8MuBVouASTMfv/OCOhAkxTudQtWzUO0d6BU/YiRT5alNwdey0dMsn3T083luLv9iG/lKKz9ewUem0RwBYOnehD6rJFXHirGDfJPHBOTSHCqHL1vQe0JLZAQwaTTieEE8zNWXwNr53BS2KxRKX8+MleoUl8LWUn6wZS/zs3auOKSRSO5pgJVq6zZCadd5D7vlhrw1KB/XfO4pv8GexAx2dbRMiGG5eumQGBcLo1RvJW2mZsGu+dQRm/NwnIpN7CP5qlkg=='
}

# Send the POST request
response = requests.post(url, headers=headers_dict, json=payload)

# Check the response
if response.status_code == 200:
    # Successful response
    print(response.text)
else:
    # Handle the error
    print(f"Request failed with status code {response.status_code}")
