# DISTÂNCIA DE lEVENSHTEIN
"""
A Distância de Levenshtein é uma medida de similaridade entre duas strings, às quais referimos como String de Origem (s)
e String de Destino (t). A distância é o número de exclusões, inserções ou substituições necessárias para transformar
s em t.
O algoritmo compara duas palavras e retorna o valor numérico que representa a distância entre elas.
"""
# Carregando Bibliotecas
import numpy as np
import copy
import pandas as pd

# Exemplo 1
# Algoritmo de Levenshtein de maneira recursiva
def levenshtein_distance_recursive(s, t):
    # Base cases
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)

    # Check if last characters are equal
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    # Recursive calls
    deletion = levenshtein_distance_recursive(s[:-1], t) + 1
    insertion = levenshtein_distance_recursive(s, t[:-1]) + 1
    substitution = levenshtein_distance_recursive(s[:-1], t[:-1]) + cost

    # Return the minimum of the three operations
    return min(deletion, insertion, substitution)


s = "kitten"
t = "sitting"
distance_1 = levenshtein_distance_recursive(s, t)
print("Distância de Levenshtein:", distance_1)
print('\n===========================================================================================================\n')


"""Para calcular a Distância de Levenshtein de uma forma não recursiva, usamos uma matriz contendo distâncias
de Levenshtein entre todos os prefixos da primeira string e todos os prefixos da segunda string"""


def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)

    # Create a matrix of size (m+1) x (n+1) initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    # Print the matrix
    for row in dp:
        print(row)

    # Return the bottom-right element of the matrix
    return dp[m][n]


s = "kitten"
t = "sitting"
distance_2 = levenshtein_distance(s, t)
print("Distância de Levenshtein:", distance_2)
print('\n===========================================================================================================\n')


# Distância de Levenshtein com vetores imprimindo o dataframe:
def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)

    # Create a matrix of size (m+1) x (n+1) initialized with 0
    dp = np.zeros((m + 1, n + 1), dtype=int)

    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    # Create a dataframe from the matrix
    df = pd.DataFrame(dp, index=list(' ' + s), columns=list(' ' + t))

    return df


s = "kitten"
t = "sitting"
distance_df = levenshtein_distance(s, t)
print("Distância de Levenshtein:\n", distance_df)
print('\n===========================================================================================================\n')


texto1 = 'Bom dia'
texto2 = 'Boa tarde'
texto3 = 'Boa noite'
texto4 = 'Boa'
terms = [texto1, texto2, texto3, texto4]

texto1_term = texto1
other_terms = [texto2, texto3, texto4]


# Distância de Levenshtein versão elaborada
def levenshtein_edit_distance(u,v):
    # convertendo em minúsculas
    u = u.lower()
    v = v.lower()
    # casos básicos
    if u == v: return 0
    elif len(u) == 0: return len(v)
    elif len(v) == 0: return len(u)
    # inicializa a matriz de distância
    edit_matrix = []
    # inicializa as duas matrizes de distância
    du = [0] * (len(v) + 1)
    dv = [0] * (len(v) + 1)
    # du: linha anterior de distância
    for i in range(len(du)):
        du[i] = i
        # du: linha anterior de distância
    for i in range(len(u)):
        dv[0] = i + 1
        # calcula o custo de acordo com o algoritmo
        for j in range(len(v)):
            cost = 0 if u[i] == v[j] else 1
            dv[j + 1] = min(dv[j] + 1, du[j + 1] +1, du[j] + cost)
        # atribui dv a du para próxima iteração
        for j in range(len(du)):
            du[j] = dv[j]
        # copia dv para a matriz de decisão
        edit_matrix.append(copy.copy(dv))
    # calcula a distância de edição final e edita a matriz
    distance = dv[len(v)]
    edit_matrix = np.array(edit_matrix)
    edit_matrix = edit_matrix.T
    edit_matrix = edit_matrix[1:,]
    edit_matrix = pd.DataFrame(data=edit_matrix,
                               index=list(v),
                               columns=list(u))
    return distance, edit_matrix


for term in other_terms:
    edit_d, edit_m = levenshtein_edit_distance(texto1_term, term)
    print('\033[1m' + 'Computando distância entre o texto:\033[0m {} e o termo: {}'.format(texto1_term, term))
    print('\033[1m' + 'A Distância de Levenshtein é: \033[0m {}'.format(edit_d))
    print('\033[4m' + 'Matriz de distância: \033[0m')
    print(edit_m)
    print('-'*30)