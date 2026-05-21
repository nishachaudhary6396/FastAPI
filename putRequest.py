import requests
r = requests.put("https://httpbin.org/put",
                 data={"name":"meet"})
print(r.text)