import requests
url = "https://example.com/bigfile.zip"
r = requests.get(url, stream=True)
with open("file.zip","wb") as fd:
    for chunk in r.iter_content(chunk_size=18):
        fd.write(chunk)