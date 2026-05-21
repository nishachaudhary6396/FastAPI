import requests
r = requests.get("https://www.codewithharry.com")
print(r.text)
with open("index.html", 'w', encoding="utf-8") as f:
    f.write(r.text)