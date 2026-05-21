import requests
r = requests.delete("https://httpbin.org/delete")
print(r.text)