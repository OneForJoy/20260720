import urllib.request
import json

print("Testing FastAPI on http://127.0.0.1:8000\n")

try:
    # Root endpoint
    url = 'http://127.0.0.1:8000/'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5) as response:
        result = json.loads(response.read().decode())
        print(f"✅ GET / -> {result}")
        
    # Encode endpoint
    url = 'http://127.0.0.1:8000/encode'
    req = urllib.request.Request(
        url=url,
        data=json.dumps({'input': 'hello world', 'text': True}).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=5) as response:
        result = json.loads(response.read().decode())
        print(f"✅ POST /encode -> {result}")
        
    # Decode endpoint
    url = 'http://127.0.0.1:8000/decode'
    req = urllib.request.Request(
        url=url,
        data=json.dumps({'input': 'AAwf93rvy4aWQVw', 'text': True}).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=5) as response:
        result = json.loads(response.read().decode())
        print(f"✅ POST /decode -> {result}")
        
    print("\n🎉 All endpoints working!")
    
except Exception as e:
    print(f"❌ Error: {e}")
