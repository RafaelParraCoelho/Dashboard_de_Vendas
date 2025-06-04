# Você pode converter este código para notebook via Jupyter
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv("data/vendas.csv", parse_dates=["Data"])

# Faturamento por mês
df["Mês"] = df["Data"].dt.to_period("M").astype(str)
faturamento_mensal = df.groupby("Mês")["Valor"].sum().reset_index()

# Gráfico de faturamento
fig1 = px.bar(faturamento_mensal, x="Mês", y="Valor", title="Faturamento Mensal")
fig1.show()

# Produtos mais vendidos
produtos = df.groupby("Produto")["Valor"].sum().sort_values(ascending=False).reset_index()
fig2 = px.pie(produtos, names="Produto", values="Valor", title="Participação por Produto")
fig2.show()

# Vendas por região
regiao = df.groupby("Região")["Valor"].sum().reset_index()
fig3 = px.bar(regiao, x="Região", y="Valor", title="Vendas por Região", color="Região")
fig3.show()
