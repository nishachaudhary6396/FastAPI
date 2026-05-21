import requests
cookies = {
    "cookies_are": "working"
}

r = requests.get(
    "https://httpbin.org/cookies",
    cookies=cookies
)
print(r.text)


#RequestCookieJar-> This is advance cookie container

jar = requests.cookies.RequestsCookieJar()
jar.set(
    "tasty_cookie",
    "yum",
    domain="httpbin.org",
    path="/cookies"
)

r=requests.get(
    "https://httpbin.org/cookies",
    cookies=jar
)
print(r.json())