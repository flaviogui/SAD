# Instalar bibliotecas necessárias (se ainda não tiver)
# pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o arquivo CSV
df = pd.read_csv(r'C:\Users\SAMSUNG\Desktop\SAD\tarefa01\Balaji Fast Food Sales.csv')

# 2. Analisar as primeiras linhas do dataframe
print(df.head())

# 3. Agrupar os dados para saber quais produtos venderam mais
produtos_mais_vendidos = df.groupby('item_name')['quantity'].sum().sort_values(ascending=False)

# 4. Mostrar o top 5 produtos mais vendidos
print("\nTop 5 produtos mais vendidos:")
print(produtos_mais_vendidos.head())

# 5. Gerar o gráfico de quantidade vendida por produto
plt.figure(figsize=(12,6))
produtos_mais_vendidos.plot(kind='bar', color='skyblue')
plt.title('Quantidade Vendida por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 6. Salvar o gráfico como imagem (opcional)
plt.savefig('produtos_mais_vendidos.png')

# 7. Exibir o gráfico
plt.show()
