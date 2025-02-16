# import requests

# x = requests.get('http://127.0.0.1:5000/login')
# print(x.content)
import requests
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'username':'Hacker','password':'11'}

session = requests.Session()
x = requests.post('http://127.0.0.1:5000/login',headers=headers,data=payload)
print(x.content)

