#!/usr/bin/env python3
"""Test FastAPI on localhost:5000"""
import time
import urllib.request
import json

print("\n⏳ Waiting for FastAPI server on localhost:5000...\n")
time.sleep(3)

tests = [
    ("GET /", "http://localhost:5000/", "GET", None),
    ("POST /encode (hello world)", "http://localhost:5000/encode", "POST", {'input': 'hello world', 'text': True}),
    ("POST /decode", "http://localhost:5000/decode", "POST", {'input': 'AAwf93rvy4aWQVw', 'text': True}),
    ("POST /decode (raw hex)", "http://localhost:5000/decode", "POST", {'input': 'AAwf93rvy4aWQVw', 'text': False, 'raw': True}),
]

print("=" * 70)
print("🌐 FASTAPI LOCALHOST TESTS (http://localhost:5000)")
print("=" * 70 + "\n")

passed = 0
failed = 0

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
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode())
            print(f"✅ {name}")
            print(f"   Status: {response.status}")
            print(f"   Response: {json.dumps(result)}\n")
            passed += 1
    except Exception as e:
        print(f"❌ {name}")
        print(f"   Error: {str(e)}\n")
        failed += 1

print("=" * 70)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 70 + "\n")

if failed == 0:
    print("✨ ALL LOCALHOST TESTS PASSED!")
else:
    print("⚠️ Some tests failed. Is the server running?")
