import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Nisha",
    "course": "Full Stack"
}
r = requests.post(
    url,
    json=payload
)
print(r.status_code)
print(r.json())