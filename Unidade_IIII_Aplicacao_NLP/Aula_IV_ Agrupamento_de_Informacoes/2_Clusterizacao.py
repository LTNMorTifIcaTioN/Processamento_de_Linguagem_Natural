# MEDIDAS DE DISTÂNCIA
"""
Medidas de Distância: São usadas para medir a similaridade entre dois ou mais vetores no espaço multidimensional.

Distância Euclidiana:
    A distância euclidiana é muito semelhante ao Teorema de Pitágoras (H^2 = A^2 + B^2).
    Seja A = (x_1, ..., x_n) e B = (y_1, ..., y_n), a distância euclidiana entre A e B é dada por:
    d(x,y) = RaizQ[(x_1 - y_1)^2 + ... + (x_n - y_n)^2]

Distância de Manhattan:
    A distância de Manhattan é calculada como a soma das diferenças absolutas entre dois pontos
    d = somatório |x_i - y_i|

Distância de Chebyshev:
    É calculado como o máximo da diferença absoluta entre os elementos dos vetores (maior valor - menor valor).

Distância de Minkowski:
    A distância de Minkowski é apenas uma forma generalizada das distâncias anteriores. A distância de Minkowski também é
    chamada de NORMA P de um vetor.

Distância de Hamming:
    A distância de Hamming mede se os dois atributos são diferentes ou não. Quando eles são iguais, a distância é 0;
    caso contrário é 1, 2, 3 e assim sucessivamente.
    Ex.:
    0000 e 1111 = a distância de Hamming é igual a 4.
    Carolina e Caroline = distância de Hamming igual a 1.

Semelhança do Cosseno
    Mede o ângulo do cosseno entre os dois vetores.
    Varia de 0 a 1, onde 1 significa que os dois vetores são perfeitamente semelhantes.
    Semelhança(A,B) = (A * B) / (||A|| * ||B||)
"""

# Carregando Bibliotecas
import math
import numpy as np
from math import sqrt

# Distância Euclidiana entre dois vetores

def euclidean_distance(a,b):
    return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))

# Vetores
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]

# Calculando a Distância Euclidiana
dist_1 = euclidean_distance(row1, row2)
print('\033[1m' +'Distância Euclidiana: ', dist_1)
print()
print('\n===========================================================================================================\n')


# Distância de Manhattan
def manhattan(x, y):
    distance=0
    for a,b in zip(x,y):
        distance += sum([abs(a-b)])
    return distance


dist_2 = manhattan(row1, row2)
print('\033[1m' +'Distância de Manhattan: ', dist_2)
print()
print('\n===========================================================================================================\n')


# Distância de Chebyshev
def chebyshev(x,y):
    distance = []
    for a,b in zip(x,y):
        distance.append(abs(a-b))
        print('\033[1m' +'Distâncias: ', distance)
    return max(distance)


dist_3 = chebyshev(row1, row2)
print('\033[1m' +'Distância de Chebychev: ', dist_3)
print()
print('\n===========================================================================================================\n')


# Distância de Hamming
def hamming(x,y):
    distance = 0
    for a,b in zip(x,y):
        if a != b:
            distance += 1
    return distance


dist_4 = hamming(row1, row2)
print('\033[1m' +'Distância de Hamming: ', dist_4)
print()
print('\n===========================================================================================================\n')

dist_4 = hamming('boa tarde pessoal', 'boa noite pessoínha')
print('\033[1m' +'Distância de Hamming: ', dist_4)
print()
print('\n===========================================================================================================\n')


# Similaridade do Cosseno numpy
def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    similarity = dot_product / (magnitude_a * magnitude_b)
    return similarity


dist_5 = cosine_similarity(row1, row2)
print('\033[1m' + 'Similaridade do Cosseno Numpy: ', dist_5)
print()
print('\n===========================================================================================================\n')


# Similaridade do Cosseno Math
def cosine_similarity_Math(x, y):
    numerator = 0
    sum_x = 0
    sum_y = 0
    for a,b in zip(x,y):
        numerator += sum([a * b])
        sum_x += sum([a**2])
        sum_y += sum([b**2])
    denominator = round(math.sqrt(sum_x) * math.sqrt(sum_y))
    return numerator / denominator


dist_5 = cosine_similarity_Math(row1, row2)
print('\033[1m' + 'Similaridade do Cosseno Math: ', dist_5)
print()
print('\n===========================================================================================================\n')