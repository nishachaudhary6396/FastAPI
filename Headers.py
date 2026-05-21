#Header are extra information sent with Http requests and responses.---metadata
import requests
url = "https://httpbin.org/get"
headers = {
    "Authorization": "Beare MY_TOKEN",
    "User-Agent": "Nisha-App/1.0",
    "Accept": "application/json"
}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.json())