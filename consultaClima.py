'''
Para fazer consultas do clima em tempo real.
Para esse code, você precisara da API Key para setar sua localização e com isso ter o clima da sua região.
Para esse caso utilizei o API da Open Weather Map.
'''

import requests
import json


cidade = input('Informe sua cidade: ')

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'(Coloque aqui a sua API Key)')

tempo = json.loads(requisicao.text)

print('Condição do tempo:', tempo['weather'][0]['main'])
print('Temperatura: ', float(tempo['main']['temp']) - 273.15)
