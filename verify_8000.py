import urllib.request
import json

try:
    url = 'http://127.0.0.1:8000/'
    with urllib.request.urlopen(url, timeout=5) as response:
        print('✅ Server is RUNNING on http://127.0.0.1:8000')
        print('Response:', response.read().decode())
except Exception as e:
    print('❌ Cannot connect:', str(e))
