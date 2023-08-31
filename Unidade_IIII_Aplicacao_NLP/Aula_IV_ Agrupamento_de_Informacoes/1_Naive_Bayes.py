# Análise de Sentimentos com Naive Bayes
"""
O Teorema de Bayes pode ser representado pela seguinte equação:
    P(A|B) = [P(B|A) * P(A)] / P(B)
"""

# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix

# Carregando o dataset
data = pd.read_csv('amazon_cells_labelled.txt', sep='\t', header=None)

# Lendo as 10 primeiras linhas do dataset
data.head(10)

# Separando as colunas que contêm texto e colunas que contêm rótulos de sentimento
X = data.iloc[:,0]  # extrai colunas com comentários
Y = data.iloc[:,-1]  # extrai colunas com sentimentos

# Pré-processamento do texto
vectorizer = CountVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# Convertendo a matriz esparsa em uma matriz densa
X_vec_dense = np.asarray(X_vec.todense())

# Transformando a contagem de palavras em seus respectivos valores tf-idf
tfidf = TfidfTransformer()
X_tfidf = tfidf.fit_transform(X_vec_dense)
X_tfidf = np.asarray(X_tfidf.todense())

# Dividindo conjunto de dados em treinamento e teste
# Dados de teste igual a 25%
X_train, X_test, Y_train, Y_test = train_test_split(X_tfidf, Y, test_size=0.25, random_state=0)

# Treinando o modelo de classificador multinomial Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, Y_train)

# Obtendo os valores de sentimento previstos
Y_pred = clf.predict(X_test)
print("Valores de sentimento previstos:")
print(Y_pred)
print()

# Criando a matriz de confusão
CM = confusion_matrix(Y_test, Y_pred)
print('Matriz de confusão:')
print(CM)
print()

# Sentimentos com pontuação igual a zero
print('Total de sentimentos com pontuação igual a zero= ', np.sum(CM[:,0]))
print()
print('Previstos corretamente =', np.sum(CM[0,0]))
print()
print('Previstos incorretamente =', np.sum(CM[1,0]))
print()

# Sentimentos com pontuação igual a um
print('Total de sentimentos com pontuação igual a um= ', np.sum(CM[:,1]))
print()
print('Previstos corretamente =', np.sum(CM[1,1]))
print()
print('Previstos incorretamente =', np.sum(CM[0,1]))
print()

# Plotando a Matriz de Confusão
fig, ax = plot_confusion_matrix(CM, figsize=(9, 9), cmap=plt.colormaps.get_cmap('Blues'))
plt.xlabel('Previsões', fontsize=14)
plt.ylabel('Verdadeiro', fontsize=14)
plt.title('Matriz de Confusão', fontsize=14)
plt.show()

# Total de sentimentos com pontuação igual a 0 e 1

sent_zero = CM[0,0]+CM[1,0]
sent_um = CM[0,1]+CM[1,1]

print('Total de sentimentos com pontuação igual a zero= ', sent_zero)
print()
print('Total de sentimentos com pontuação igual a um= ', sent_um)
print()

# Total de previsões corretas
print('Total de previsões corretas =', np.trace(CM))
print()

# Total de previsões
print('Total de previsões =', np.sum(CM))
print()

# Calculando a precisão do modelo
# Total de previsões corretas / total de previsões
precisao = np.trace(CM)/np.sum(CM)
print(f'Precisão do Modelo = {precisao: .2%}')
