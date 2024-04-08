import pandas as pd

# Carregando a planilha Excel
dados = pd.read_excel('USER.xlsx')


# Verificando os nomes que não possuem "ok" na coluna "Cartão1"
nomes_sem_ok = dados.loc[dados['Cartão1'] != 'ok', 'Nome']



# Exibindo os nomes
print(nomes_sem_ok)

# Exportando os nomes para um arquivo CSV
nomes_sem_ok.to_csv('nomes_faltantes.csv', index=False)

import os

# Nome do arquivo CSV
nome_arquivo_csv = 'nomes_faltantes.csv'

# Nome do arquivo TXT (destino)
nome_arquivo_txt = 'nomes_faltantes.txt'

# Verificar se o arquivo de destino já existe
if os.path.exists(nome_arquivo_txt):
    # Remover o arquivo de destino
    os.remove(nome_arquivo_txt)

# Renomear o arquivo CSV para TXT
os.rename(nome_arquivo_csv, nome_arquivo_txt)

