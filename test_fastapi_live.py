#!/usr/bin/env python3
import time
import urllib.request
import json

print("Waiting for FastAPI server to start...\n")
time.sleep(4)

tests = [
    ("GET /", "http://127.0.0.1:8000/", "GET", None),
    ("POST /encode", "http://127.0.0.1:8000/encode", "POST", {'input': 'hello fastapi', 'text': True}),
    ("POST /decode", "http://127.0.0.1:8000/decode", "POST", {'input': 'AAwf93rvy4aWQVw', 'text': True}),
]

print("🚀 Testing FastAPI on http://127.0.0.1:8000\n")
print("=" * 60)

for name, url, method, body in tests:
    try:
        if method == "GET":
            req = urllib.request.Request(url, method='GET')
        else:
            data = json.dumps(body).encode('utf-8')
            req = urllib.request.Request(
                url=url,
                data=data,
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
        
        with urllib.request.urlopen(req, timeout=5) as response:
            result = json.loads(response.read().decode())
            print(f"✅ {name}")
            print(f"   Response: {json.dumps(result, indent=6)}")
            print()
    except Exception as e:
        print(f"❌ {name}")
        print(f"   Error: {str(e)}")
        print()

print("=" * 60)
print("✨ FastAPI testing complete!")
