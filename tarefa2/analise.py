import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de visualização
sns.set(style="whitegrid")

# Caminho do arquivo CSV
file_path = r'C:\Users\SAMSUNG\Desktop\SAD\tarefa2\sales_data_sample.csv'

# Carregando o dataset
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Exibir o dataset completo
pd.set_option('display.max_rows', None)
print("### DATASET COMPLETO ###\n")
print(df)

# --------------------------
# ANÁLISE 1: VENDAS POR LINHA DE PRODUTO
# --------------------------
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().reset_index().sort_values(by='SALES', ascending=False)

# Gráfico de vendas por linha de produto
plt.figure(figsize=(10, 6))
sns.barplot(x='SALES', y='PRODUCTLINE', data=product_sales, palette='Blues_d')
plt.title('Vendas Totais por Linha de Produto')
plt.xlabel('Total de Vendas')
plt.ylabel('Linha de Produto')
plt.tight_layout()
plt.show()

# Insight 1
top_product = product_sales.iloc[0]
print(f"\n🔍 INSIGHT 1:\nA linha de produto com maior faturamento foi **{top_product['PRODUCTLINE']}**, com um total de vendas de **${top_product['SALES']:.2f}**.")

# --------------------------
# ANÁLISE 2: VENDAS POR PAÍS
# --------------------------
country_sales = df.groupby('COUNTRY')['SALES'].sum().reset_index().sort_values(by='SALES', ascending=False)

# Gráfico de vendas por país
plt.figure(figsize=(12, 6))
sns.barplot(x='COUNTRY', y='SALES', data=country_sales, palette='Greens_d')
plt.title('Vendas Totais por País')
plt.xlabel('País')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insight 2
top_country = country_sales.iloc[0]
print(f"\n🔍 INSIGHT 2:\nO país com maior volume de vendas foi **{top_country['COUNTRY']}**, com um total de **${top_country['SALES']:.2f}**.")
