'''
 Novas Perguntas do CEO para você:
1. Quantas casas estão disponíveis para compra?
2. Quantos atributos as casas possuem?
3. Quais são os atributos das casas?
4. Qual a casa mais cara ( casa com o maior valor de venda )?
5. Qual a casa com o maior número de quartos?
6. Qual a soma total de quartos do conjunto de dados?
7. Quantas casas possuem 2 banheiros?
8. Qual o preço médio de todas as casas no conjunto de dados?
9. Qual o preço médio de casas com 2 banheiros?
10. Qual o preço mínimo entre as casas com 3 quartos?
11. Quantas casas possuem mais de 300 metros quadrados na sala 
de estar?
12. Quantas casas tem mais de 2 andares?
13. Quantas casas tem vista para o mar?
14. Das casas com vista para o mar, quantas tem 3 quartos?
15. Das casas com mais de 300 metros quadrados de sala de estar, 
quantas tem mais de 2 banheiros?'''


import pandas as pd

#data = pd.read_csv('Aula 01 - Começando com Python do ZERO/kc_house_data.csv')
data = pd.read_csv("kc_house_data.csv")

#mostrar as 5 primeiras linhas
print(data.head())

#mostrar o numero de colunas eo numero de linhas do cojunto de dados
print(data.shape)

#mostrar o nome das colunas do conjunto de dados
print(data.columns)

#mostrar o conjunto de dados pela coluna Price
#print(data[['id', 'price']].sort_values('price'))

#mostar o conjunto de dados ordenados pela coluna Price do maior para o menor
#print(data[['id', 'price']].sort_values('price', ascending=False))

# 1. Quantas casas estão disponíveis para compra?
print(f"Estão disponíveis para compra: {len(data['id'].unique())} imoveis.")
print(f"Estão disponíveis para compra: {len(data['id'].drop_duplicates())} imoveis.")

# 2. Quantos atributos as casas possuem?
# Considereando que as Colunas id e date não são atributos das casas
print(f"Os imóveis possuem {len(data.drop(['id', 'date'], axis=1).columns)} atributos")

# 3. Quais são os atributos das casas?
print(f"Os imóveis possuem os seguintes atributos:\n {data.drop(['id', 'date'], axis=1).columns}")

# 4. Qual a casa mais cara ( casa com o maior valor de venda )?
print(f"{data[['id', 'price']].sort_values('price', ascending=False)}")
casa_id = data[['id', 'price']].sort_values('price', ascending=False).reset_index(drop=True).loc[0, 'id']
casa_valor = data[['id', 'price']].sort_values('price', ascending=False).reset_index(drop=True).loc[0, 'price']
print(f'A casa que possui o maior valor é a de ID: {casa_id} e valor de {casa_valor}')

# 5. Qual a casa com o maior número de quartos?
print(data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False).head())