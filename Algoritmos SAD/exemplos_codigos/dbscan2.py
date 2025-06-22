from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np

# Gera dados normais (transações legítimas)
X, _ = make_blobs(n_samples=300, centers=2, cluster_std=0.60, random_state=42)

# Adiciona anomalias (fraudes)
anomalias = np.random.uniform(low=-6, high=10, size=(10, 2))
X = np.vstack([X, anomalias])

# Normaliza
X = StandardScaler().fit_transform(X)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)

# Visualiza: -1 são as anomalias detectadas
cores = np.array(['#1f77b4', '#ff7f0e', '#2ca02c', 'red'])  # última cor: anomalias

plt.figure(figsize=(8, 6))
for i in np.unique(labels):
    plt.scatter(X[labels == i, 0], X[labels == i, 1],
                label=f'Grupo {i}' if i != -1 else 'Anomalias',
                color='red' if i == -1 else None)

plt.title("Detecção de Anomalias com DBSCAN")
plt.xlabel("Frequência da transação (normalizada)")
plt.ylabel("Valor da transação (normalizado)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
