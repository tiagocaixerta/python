import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sys import argv

def extrair_dados():
    """
    Função para extrair os dados e salvar no arquivo CSV `taxa-cdi.csv`.
    (Substitua este exemplo com o código de extração real)
    """
    dados = [
        {'hora': '09:00', 'taxa': 0.1},
        {'hora': '10:00', 'taxa': 0.12},
        {'hora': '11:00', 'taxa': 0.11},
        {'hora': '12:00', 'taxa': 0.13},
        {'hora': '13:00', 'taxa': 0.15}
    ]
    with open('taxa-cdi.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['hora', 'taxa'])
        writer.writeheader()
        writer.writerows(dados)
    print("Arquivo taxa-cdi.csv gerado com sucesso.")

def gerar_grafico(nome_grafico):
    """
    Função para gerar o gráfico com base nos dados do arquivo `taxa-cdi.csv`.
    Salva o gráfico em um arquivo PNG com o nome especificado pelo usuário.
    """
    df = pd.read_csv('taxa-cdi.csv')

  
    plt.figure(figsize=(10, 6))
    grafico = sns.lineplot(x=df['hora'], y=df['taxa'], marker="o")
    grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.set(title='Taxa CDI ao longo do tempo', xlabel='Hora', ylabel='Taxa CDI')

    grafico.get_figure().savefig(f"{nome_grafico}.png", bbox_inches="tight")
    print(f"Gráfico salvo como {nome_grafico}.png")

def main():
    if len(argv) < 2:
        print("Erro: Você deve fornecer o nome do arquivo para o gráfico.")
        print("Exemplo de uso: python analise.py nome-do-grafico")
        exit(1)

    nome_grafico = argv[1]

 
    extrair_dados()
    gerar_grafico(nome_grafico)

if __name__ == "__main__":
    main()
