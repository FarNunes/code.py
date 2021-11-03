'''
Para fazer consultar a cotação do dollar em tempo real.
'''

import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(requisicao.text)

    print('### Cotação ###', datetime.datetime.now())
    print('Dolar:', cotacao['USDBRL']['high'])
    print('Variação do Dolar:', cotacao['USDBRL']['varBid'])
    print('Euro:', cotacao['EURBRL']['high'])
    print('Variação do Euro:', cotacao['EURBRL']['varBid'])
    print('BitCoin:', cotacao['BTCBRL']['high'])
    print('Variação do BitCoin:', cotacao['BTCBRL']['varBid'])
    time.sleep(30)
