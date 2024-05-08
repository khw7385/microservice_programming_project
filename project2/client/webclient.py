import requests

response = requests.get('http://webserver:5001')

print(response.text)
