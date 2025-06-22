import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

# Carrega e normaliza os dados do Iris
data = load_iris()
X = data.data
X = MinMaxScaler().fit_transform(X)

# Cria e treina o SOM
som = MiniSom(x=10, y=10, input_len=4, sigma=1.0, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(data=X, num_iteration=1000)

# Cria mapa de frequência de ativações (quantos dados foram mapeados para cada célula)
frequencia = np.zeros((10, 10))
for x in X:
    i, j = som.winner(x)
    frequencia[i][j] += 1

# Plota a grade de calor (quantidade de dados por célula)
plt.figure(figsize=(8, 6))
plt.title("Exemplo Visual: Agrupamento com SOM (Grade 10x10)")
plt.imshow(frequencia.T, cmap='Reds', origin='lower')
plt.colorbar(label="Número de dados representados")
plt.xticks(np.arange(10))
plt.yticks(np.arange(10))
plt.grid(True, color='black', linewidth=1)
plt.xlabel("Posição na grade (X)")
plt.ylabel("Posição na grade (Y)")
plt.tight_layout()
plt.show()
