import requests

response = requests.get("http://127.0.0.1:5000/config")
print(response.json())

import requests

response = requests.get("http://127.0.0.1:5000/robots")
print(response.json())
