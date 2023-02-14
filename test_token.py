import requests

# TOKEN = 'f55be97c00924f45879600ddb89e2c78a47a452f'

JWT_ACCESS_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2MzQ1MTg1LCJpYXQiOjE2NzYzNDQ4ODUsImp0aSI6IjM5MjljZDJhODcyODRiOWRhZjViODVmMWQ4NmFhODE3IiwidXNlcl9pZCI6Mn0.8h9anrrv4SpYvUrS2ojH5kpNKBlrHtykZsVD6XWFEvQ"
)
headers = {
    # 'Authorization': f'Token {TOKEN}', # Token 인증
    'Authorization': f'Bearer {JWT_ACCESS_TOKEN}', # simple-jwt Token 인증
}

res = requests.get('http://localhost:8000/post/1/', headers=headers)
print(res.json())