# Bias
"""
Chamamos de bias a diferença entre a previsão média de nosso modelo e o valor correto que
estamos tentando prever. O modelo com alta polarização presta muito pouca atenção aos dados
de treinamento e simplifica demais o modelo. Isso sempre leva a um alto erro nos dados de
treinamento e teste.
"""

# Variância
"""
Variância é a variabilidade da previsão do modelo para determinado ponto de dados ou um valor 
que nos informa a disseminação de nossos dados. O modelo com alta variação dá muita atenção 
aos dados de treinamento e não generaliza sobre os dados que não viu antes. Como resultado, 
modelos desse tipo funcionam muito bem em dados de treinamento, mas apresentam altas taxas de 
erros em dados de teste.
"""

# Overfitting
"""
De acordo com Alpaydin (2016), o termo overfitting refere-se a um modelo que se ajusta muito 
bem aos dados com os quais é treinado, mas mal os generaliza, fazendo com que, 
ao se deparar com valores diferentes dos de treinamento, os preveja com baixa precisão.
"""

# Underfitting
"""
Por outro lado, o underfitting refere-se ao estado oposto, o que significa que o modelo não se 
ajusta bem nem mesmo aos dados com os quais é treinado.

Ao relacionar overfitting e underfitting, analisando os conceitos apresentados, fica claro que:

Um modelo com baixa variância e baixo bias é o ideal.
Um modelo com baixo bias e alta variância é um modelo com overfitting.
Um modelo com alta tendência e baixa variância é geralmente um modelo de subajuste.
Um modelo com alta tendência e alta variância é o pior cenário, pois produz o maior erro de 
previsão possível.
"""


# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
rcParams['figure.figsize'] = (20, 10)
plt.rcParams['legend.fontsize'] = 13


# Definindo a função cosseno
def true_fun(x):
    return np.cos(1.5 * np.pi * x)


# Gerando valores aleatórios
np.random.seed(0)


# Definindo o número de amostras e os graus dos polinômios
n_samples = 30
degrees = [1, 4, 15]


# Gerando um array aleatório para x e y
X = np.sort(np.random.rand(n_samples))
Y = true_fun(X) + np.random.randn(n_samples) * 0.1


# Plotando o gráfico
plt.title('Gráfico com as amostras')
plt.plot(X, Y, color='red', label='Atual')
plt.scatter(X, Y, color='darkblue', s=40, label='Amostras')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


# Cria a sequencia de números uniformemente espaçados entre 0 e 1.
x1 = np.linspace(0, 1, 100)


# Aumentando a dimensão da matriz
x1 = x1[:, np.newaxis]
print(x1)


# Aplicando a regressão linear
model = LinearRegression()
model.fit(X[:, np.newaxis], Y)


# Fazendo as previsões para x1
y_pred = model.predict(x1)


# Plotando o gráfico
plt.title('Exemplo de underfitting')
plt.plot(X, Y, color='red', label='Atual')
plt.scatter(X, Y, color='darkblue', s=40, label='Amostras')
plt.plot(x1, y_pred, color='black', label='Modelo')
plt.annotate('Podemos ver que a linha reta não é capaz de capturar os padrões nos dados.',
             xy=(0.4, 0.0))
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.show()


# Plotando os Gráficos de polinômios
plt.figure(figsize=(14,5))
for i in range(len(degrees)):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())
    polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([('polynomial_features', polynomial_features), ('linear_regression',
                                                                        linear_regression)])
    pipeline.fit(X[:, np.newaxis], Y)

    # Avaliação dos modelos usando a validação cruzada
    scores = cross_val_score(pipeline, X[:, np.newaxis], Y, scoring='neg_mean_squared_error', cv=10)
    X_test = np.linspace(0, 1, 100)
    Y_poly_pred = pipeline.predict(X_test[:, np.newaxis])
    plt.plot(X_test, Y_poly_pred, label='Modelo')
    plt.plot(X_test, true_fun(X_test), label='Função verdadeira')
    plt.scatter(X, Y, edgecolors='b', s=20, label='Amostras')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc='best')
    #plt.title('Grau {}\nMSE = {:.5}(+/- {:.5})'.format(degrees[i], -scores.mean(), scores.std()))
    plt.title(f'Grau {degrees[i]}\nMSE = {-scores.mean():.5}(+/- {scores.std():.5})')
    plt.show()