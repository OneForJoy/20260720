import urllib.request
import json

# Test root endpoint
url = 'http://127.0.0.1:8080/'
with urllib.request.urlopen(url, timeout=5) as response:
    print('GET / ->', response.read().decode())

# Test encode endpoint
url = 'http://127.0.0.1:8080/encode'
req = urllib.request.Request(
    url=url,
    data=json.dumps({'input': 'hello world', 'text': True}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=5) as response:
    print('POST /encode ->', response.read().decode())

# Test decode endpoint
url = 'http://127.0.0.1:8080/decode'
req = urllib.request.Request(
    url=url,
    data=json.dumps({'input': 'AAwf93rvy4aWQVw', 'text': True}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=5) as response:
    print('POST /decode ->', response.read().decode())
