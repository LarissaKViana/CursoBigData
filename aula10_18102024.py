###AULA10 - 18/10/2024###
#
# Pandas
#
import pandas as pd #(pd=alias)
print(pd.__version__)

#CRIAÇÃO DE UM DATASET:

data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'],
        'Salário': [4500, 9000, 2000]}
df = pd.DataFrame(data)
print(df)

#CRIAÇÃO DE UMA SÉRIE:

cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
print(cargos)

#ATIVIDADE ASSISTIDA:

#Crie um dataset de 3 colunas com as seguintes informações: 'nome de um filme', 'ano de lançamento' e 'gênero'.

import pandas as pd
print(pd.__version__)

data_cinema={'nome de um filme':['As Branquelas','Enrolados','Cinderela','Encantada'],
        'ano de lançamento':[2004,2010,1950,2007],
        'gênero':['Comédia/Crime','Infantil/Musical','Infantil/Musical','Infantil/Comédia']
}

cinema=pd.DataFrame(data_cinema)
print(cinema)

#ACESSO À DATASETS EXTERNOS:

https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data

import pandas as pd
print(pd.__version__)

df_disco = pd.read_csv('ClassicDisco.csv')
# print(df_disco.head())  # Exibe as cinos primeiras linhas
print(df_disco.tail())
#Leitura de Arquivos e Filtragem:

#to_string(): #Exibe o DataFrame completo como uma string, útil para visualização.
print(df_disco.to_string())

max_rows: #Define o número máximo de linhas a ser exibido.

#Leitura de Arquivos e Filtragem:

to_string(): #Exibe o DataFrame completo como uma string, útil para visualização.

max_rows: #Define o número máximo de linhas a ser exibido.

#Filtragem de Dados: #Exemplo de filtragem por colunas e linhas específicas:

df_filtrado = df_disco[df_disco['Artista'] == 'Bee Gees']
print(df_filtrado)

#Criação de Novas Colunas: adicionar colunas derivadas

df_disco['Duração_Minutos'] = df_disco['Duração_Segundos'] / 60

#Leitura de Arquivos Excel e Outros Formatos:
###
#Atividade Prática:
###