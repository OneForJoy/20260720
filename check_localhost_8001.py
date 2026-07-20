import urllib.request

url = 'http://127.0.0.1:8001/'
with urllib.request.urlopen(url, timeout=5) as response:
    print(response.read().decode())
