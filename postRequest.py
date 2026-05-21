import requests
r = requests.post("https://httpbin.org/post",data={"name":"Nisha"})
print(r.text)