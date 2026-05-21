#Return only headers..not body/content
import requests
r = requests.head("https://httpbin.org/get")
print(r.headers)