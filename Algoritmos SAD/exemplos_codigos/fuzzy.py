import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import skfuzzy as fuzz

# Criar dados simulados (150 amostras, 3 clusters)
X, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.0, random_state=42)

# Transpor para o formato esperado pelo scikit-fuzzy (features x samples)
data = X.T

# Número de clusters
n_clusters = 3

# Executar Fuzzy C-Means
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data, c=n_clusters, m=2, error=0.005, maxiter=1000, init=None)

# 'u' é a matriz de pertinência (clusters x samples)
cluster_labels = np.argmax(u, axis=0)

# Plotar
colors = ['b', 'orange', 'g']

for j in range(n_clusters):
    # Pontos pertencentes ao cluster j (com maior pertinência)
    plt.scatter(X[cluster_labels == j, 0], X[cluster_labels == j, 1], color=colors[j], alpha=0.6, label=f'Cluster {j+1}')
    
# Plotar centros
plt.scatter(cntr[:, 0], cntr[:, 1], marker='X', s=200, c='red', label='Centros')

plt.title('Agrupamento Fuzzy (Fuzzy C-Means) com scikit-fuzzy')
plt.xlabel('Sintoma 1 (ex: Dor)')
plt.ylabel('Sintoma 2 (ex: Febre)')
plt.legend()
plt.grid(True)
plt.show()
