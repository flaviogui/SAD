from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

# Simulando coordenadas GPS
np.random.seed(0)
centros = [[1, 1], [5, 5], [9, 1]]
X = np.vstack([np.random.normal(loc=center, scale=0.4, size=(30, 2)) for center in centros])
X = np.vstack([X, np.random.uniform(low=0, high=10, size=(10, 2))])  # ruído

# Aplicando DBSCAN
db = DBSCAN(eps=0.8, min_samples=5)
labels = db.fit_predict(X)

# Visualização
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10')
plt.title("Zonas turísticas agrupadas com DBSCAN")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
