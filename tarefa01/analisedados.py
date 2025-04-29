# Instale essas bibliotecas antes se precisar:
# pip install pandas matplotlib openpyxl

import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o arquivo CSV (ajuste o caminho se necessário)
df = pd.read_csv(r'C:\Users\SAMSUNG\Desktop\SAD\tarefa01\Balaji Fast Food Sales.csv')

# 2. Configurar o pandas para mostrar tudo no terminal
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 3. Mostrar a tabela completa no terminal
print("\n=== Tabela Completa ===")
print(df)

# 4. Salvar a tabela completa como Excel (.xlsx)
excel_path = r'C:\Users\SAMSUNG\Desktop\SAD\tarefa01\Balaji_Fast_Food_Sales.xlsx'
df.to_excel(excel_path, index=False)
print(f"\nArquivo Excel salvo em: {excel_path}")

# 5. Análise: Produtos mais vendidos
produtos_mais_vendidos = df.groupby('item_name')['quantity'].sum().sort_values(ascending=False)

# 6. Mostrar o Top 5 produtos mais vendidos
print("\n=== Top 5 Produtos Mais Vendidos ===")
print(produtos_mais_vendidos.head())

# 7. Gerar o gráfico
plt.figure(figsize=(12,6))
produtos_mais_vendidos.plot(kind='bar', color='skyblue')
plt.title('Quantidade Vendida por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 8. Salvar o gráfico como imagem
grafico_path = r'C:\Users\SAMSUNG\Desktop\SAD\tarefa01\produtos_mais_vendidos.png'
plt.savefig(grafico_path)
print(f"\nGráfico salvo em: {grafico_path}")

# 9. Mostrar o gráfico na tela
plt.show()
