'''
Para fazer consultas em tempo real twitter via IDE.
Para esse caso necessitamos da API do twitter, e com isso você após cadastrar recebera as keys solicitadas no codigo abaixo.
'''

import oauth2
import json
import urllib.parse

consumer_key = input('Coloque sua key: ')
consumer_secret = input('Coloque sua secret key: ')
token_key = input('Coloque seu token: ')
token_secret_key = input('Coloque seu secret key token: ')

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret_key)
cliente = oauth2.Client(consumer, token)

query = input('Pesquisa: ')
query_codificada = urllib.parse.quote(query, safe='') #transformar na url especial que pode buscar caracteres especiais como: - # $ (acento)
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')
decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twitt in twittes:
    print(twitt['user']['screen_name'])
    print(twitt['text'])
    print()
