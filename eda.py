import pandas as pd

df = pd.read_csv("dados_vendas.csv")

# Verificando estatísticas básicas
# print(df.describe())
# print(df.info())

# Calculando quantas vendas foram feitas por categoria a partir da quantidade
categorias_vendas = df.groupby('categoria')['quantidade'].sum().reset_index()

# Calculando quanto cada loja esta faturando
lojas_faturamento = df.groupby('loja')['valor_total'].sum().reset_index()

# Calculando quais os produtos mais vendidos a partir da quantidade
produtos_vendas = df.groupby('produto')['quantidade'].sum().reset_index()

# Separando qual foi o produto mais vendido
produto_mais_vendido = produtos_vendas.sort_values(by=["quantidade"], ascending=False).head(1)

# Calculando o ticket medio da empresa
ticket_medio = round(df['valor_total'].mean(), 2)

# Calculando o montante arrecadado a partir das vendas de cada categoria de produto
receita_por_categoria = df.groupby('categoria')['valor_total'].sum().reset_index()

# Analisando a evolução das vendas ao longo dos meses
df['data'] = pd.to_datetime(df['data'])
df['ano_mes'] = df['data'].dt.to_period('M')
df_mensal = df.groupby('ano_mes')['valor_total'].sum().reset_index()



