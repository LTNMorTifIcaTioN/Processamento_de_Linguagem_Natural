# APRENDIZADO NÃO SUPERVISIONADO
"""
> É uma técnica em machine learning usada para encontrar padrões em dados. Os dados fornecidos não são rotulados.
> Os Algoritmos são deixados para encontrar resultados por conta própria.
> é um tipo de aprendizado de máquina que procura padrões préviamente desconhecidos em um conjunto de dados
não rotulados e sem a interação humana.
> Os métodos mais proeminentes de Aprendizagem não supervisionada são:
    Análise de agrupamento.
    Análise de componentes principais.
> Na aprendizagem não supervisionada as entradas são segregadas com base nos recursos. A previsão é baseada em qual
cluster ela pertence.

Características:
> Feature: Variável de entrada usada para fazer previsões.
> Predições: A saída de um modelo quando fornecida com um exemplo de entrada.
> Exemplo: Uma linha do conjunto de dados. Um exemplo contém um ou mais recursos e possivelmente um rótulo.
> Rótulo: (label) resultado do recurso.
"""

# Exemplo Algoritmo DBSCAN

# Importando bibliotecas
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

# Carregando o dataset
iris = load_iris()

#Declarando o modelo DBSCAN
dbscan = DBSCAN()

#Treinamento
dbscan.fit(iris.data)

#Utilizando o PCA
pca = PCA(n_components=2)
pca.fit(iris.data)
pca_2d = pca.transform(iris.data)

#Criando cada cluster com base na classe
c1 = None
c2 = None
c3 = None

for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

#Definindo o tamanho da figura
rcParams['figure.figsize'] = (20, 10)
plt.rcParams['legend.fontsize'] = 13

#Plotando os clusters com base na classe
plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Ruido'])
plt.title('DBSCAN encontrou 2 clusters e ruido')
plt.show()