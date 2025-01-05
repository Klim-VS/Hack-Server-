import requests

x = requests.get('http://127.0.0.1:5000/data')
print(x.content)