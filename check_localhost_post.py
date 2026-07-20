import json
import urllib.request

base_url = 'http://127.0.0.1:8000'

req = urllib.request.Request(
    url=f'{base_url}/encode',
    data=json.dumps({'input': 'hello world', 'text': True}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=5) as response:
    print('encode:', response.read().decode())

req = urllib.request.Request(
    url=f'{base_url}/decode',
    data=json.dumps({'input': 'AAwf93rvy4aWQVw', 'text': True}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=5) as response:
    print('decode:', response.read().decode())
