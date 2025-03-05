import streamlit as st
import plotly.express as px
from eda import *

# Utilizando funções da lib para tornar a visualização dos dados mais agradável
st.set_page_config(page_title="Dados de vendas",layout='wide')
st.title("Simulação de dados de vendas")
st.subheader('Explorando dados com Python: Análise de vendas de uma rede de lojas de produtos eletrônicos e variedades')

# Determinando as colunas onde cada uma das informações irá aparecer em tela
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Ilustrando a receita total por loja a partir de um gráfico de barras
fig_loja = px.bar(lojas_faturamento, x='loja', y='valor_total', title='Receita total por loja', labels={
    'loja': 'Loja', 'valor_total': 'Faturamento'})
col1.plotly_chart(fig_loja)

# Ilustrando o percentual de vendas por categoria a partir de um gráfico de pizza
fig_categoria = px.pie(categorias_vendas, names='categoria', values='quantidade', title='Percentual de vendas por categoria')
fig_categoria.update_traces(textinfo='percent+label')
col2.plotly_chart(fig_categoria)

# Ilustrando os itens mais vendidos a partir de um gráfico de barras
fig_itens_mais_vendidos = px.bar(produtos_vendas, x='produto', y='quantidade', title='Itens mais vendidos', labels={
    'produto': 'Produto', 'quantidade': 'Quantidade'})
col3.plotly_chart(fig_itens_mais_vendidos)

# Ilustrando as categorias que geraram maior receita a partir de um gráfico de barras
fig_categorias_mais_vendidas = px.bar(receita_por_categoria, x='categoria', y='valor_total', title='Categorias que geraram maior receita', labels={
    'categoria': 'Categoria', 'valor_total': 'Receita'})
col4.plotly_chart(fig_categorias_mais_vendidas)