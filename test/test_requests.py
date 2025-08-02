import requests

url = "https://your-ngrok-url.ngrok-free.app/generate"
payload = {"business_description": "eco-friendly coffee shop"}

res = requests.post(url, json=payload)
print(res.status_code)
print(res.json())
