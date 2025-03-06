import pandas as pd
import numpy as np

# Definindo as variáveis com categorias de produtos, os preços dos produtos e as lojas
produtos = {
    "Notebook": "Eletrônicos",
    "Smartphone": "Eletrônicos",
    "Tablet": "Eletrônicos",
    "Cadeira Gamer": "Móveis",
    "Mesa de Escritório": "Móveis",
    "Monitor": "Eletrônicos",
    "Teclado Mecânico": "Acessórios",
    "Mouse Gamer": "Acessórios",
    "Headset": "Acessórios",
    "Impressora": "Periféricos",
    "Câmera de Segurança": "Periféricos"
}

preco_produtos = {
    "Notebook": np.round(np.random.uniform(1500, 3000), 2),
    "Smartphone": np.round(np.random.uniform(1500, 3000), 2),
    "Tablet": np.round(np.random.uniform(700, 1500), 2),
    "Cadeira Gamer": np.round(np.random.uniform(1000, 2000), 2),
    "Mesa de Escritório": np.round(np.random.uniform(1500, 3000), 2),
    "Monitor": np.round(np.random.uniform(500, 2000), 2),
    "Teclado Mecânico": np.round(np.random.uniform(200, 730), 2),
    "Mouse Gamer": np.round(np.random.uniform(100, 600), 2),
    "Headset": np.round(np.random.uniform(150, 800), 2),
    "Impressora": np.round(np.random.uniform(350, 2000), 2),
    "Câmera de Segurança": np.round(np.random.uniform(250, 950), 2)
}

lojas = ["Loja Centro", "Loja Norte", "Loja Sul", "Loja Leste"]

# Gerando 500 vendas fictícias
np.random.seed(42)  # Para reprodutibilidade
num_vendas = 500

# Gerador de produtos aleatorios
produtos_aleatorios = np.random.choice(list(produtos.keys()), size=num_vendas)

# Estruturando dados que aparecerão no arquivo CSV
dados = {
    "id_venda": np.arange(1, num_vendas + 1),
    "data": pd.date_range(start="2024-01-01", periods=num_vendas, freq="D"),
    "produto": produtos_aleatorios,
    "categoria": [produtos[p] for p in produtos_aleatorios],
    "preco_unitario": [preco_produtos[p] for p in produtos_aleatorios],
    "quantidade": np.random.randint(1, 10, num_vendas),
    "loja": np.random.choice(lojas, num_vendas),
}

# Criando DataFrame a partir dos dados e adicionando a coluna de valor total
df = pd.DataFrame(dados)
df["valor_total"] = round(df["preco_unitario"] * df["quantidade"], 2)

# Salvando em CSV para futuras análises
df.to_csv("dados_vendas.csv", index=False)
