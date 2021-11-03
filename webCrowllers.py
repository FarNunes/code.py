'''
Achar e-mails diretamente do site - (Web Crowllers)
'''

import re
import requests

requisicao = requests.get(input('Informe o site desejado:'))

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Contato não encontrado')