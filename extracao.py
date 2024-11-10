import os
import time
import json
from random import random
from datetime import datetime
import requests

import requests

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

try:
    response = requests.get(URL)
    response.raise_for_status()  
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Erro de conexão. Verifique a URL ou sua conexão de rede.")
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")



URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'


if os.path.exists('taxa-cdi.csv'):
    os.remove('taxa-cdi.csv')


for _ in range(10):
   
    data_e_hora = datetime.now()
    data = datetime.strftime(data_e_hora, '%Y/%m/%d')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')
    
   
    try:
        response = requests.get(URL)
        response.raise_for_status()  
    except requests.HTTPError:
        print("Dado não encontrado, continuando.")
        cdi = None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        dado = json.loads(response.text)
        cdi = float(dado['taxa'].replace(',', '.')) + (random() - 0.5)  
    
  
    if not os.path.exists('taxa-cdi.csv'):
        with open('taxa-cdi.csv', mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')
    
   
    with open('taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')
    
   
    time.sleep(2 + (random() - 0.5))

print("Sucesso! O arquivo taxa-cdi.csv foi gerado.")
