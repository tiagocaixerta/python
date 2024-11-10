import os
import time
import json
from random import random
from datetime import datetime
import requests

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados?formato=json'

try:
    response = requests.get(URL)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.ConnectionError:
    print("Erro de conexão. Verifique a URL ou sua conexão de rede.")
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")

# Verifica se o arquivo taxa-cdi.csv existe e o remove, se necessário
if os.path.exists('taxa-cdi.csv'):
    os.remove('taxa-cdi.csv')

# Executa a coleta dos dados 10 vezes
for _ in range(10):
    # Captura a data e hora atuais
    data_e_hora = datetime.now()
    data = data_e_hora.strftime('%Y/%m/%d')
    hora = data_e_hora.strftime('%H:%M:%S')

    # Realiza a requisição e tenta processar a taxa CDI
    try:
        response = requests.get(URL)
        response.raise_for_status()
        dados = json.loads(response.text)

        # Obtém a taxa CDI e adiciona um pequeno ajuste aleatório
        cdi = float(dados[-1].get('valor', '0').replace(',', '.')) + (random() - 0.5)
    except (requests.HTTPError, ValueError, IndexError):
        print("Erro ao processar o dado da taxa CDI. Continuando.")
        cdi = None
    except Exception as exc:
        print("Erro inesperado, parando a execução.")
        raise exc

    # Cria o arquivo CSV e escreve o cabeçalho, se ele ainda não existir
    if not os.path.exists('taxa-cdi.csv'):
        with open('taxa-cdi.csv', mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')

    # Adiciona os dados ao arquivo CSV
    with open('taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')

    # Aguarda antes da próxima execução
    time.sleep(2 + (random() - 0.5))

print("Sucesso! O arquivo taxa-cdi.csv foi gerado.")
