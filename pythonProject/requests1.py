import requests
response = requests.get('https://viacep.com.br/ws/53900000/json/')

print(response.text)
print(response.json())