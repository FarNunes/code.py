import requests
import json

# Api key: f82d01a916d7f21a797a32f5169b98ec // 9c16bc51194b4575d0da080ef765264d

cidade = input('Informe sua cidade: ')

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=9c16bc51194b4575d0da080ef765264d')

tempo = json.loads(requisicao.text)

print('Condição do tempo:', tempo['weather'][0]['main'])
print('Temperatura: ', float(tempo['main']['temp']) - 273.15)