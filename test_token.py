import requests

TOKEN = 'f55be97c00924f45879600ddb89e2c78a47a452f'

headers = {
    'Authorization': f'Token {TOKEN}',
}

res = requests.get('http://localhost:8000/post/1/', headers=headers)
print(res.json())