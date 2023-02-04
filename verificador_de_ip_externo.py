import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']

print("Detalhes do IP Externo")

print(f"IP: {ip}")
print(f"Organização: {org}")
print(f"Cidade: {city}")
print(f"País: {country}")
print(f"Região: {region}")