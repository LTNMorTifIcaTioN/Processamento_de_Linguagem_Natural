# APRENDIZAGEM SUPERVISIONADA
"""
A aprendizagem supervisionada geralmente pode ser vista como uma tarefa de classificação ou equivalentemente,
como uma tarefa de ajuste de função, onde extrapola-se a forma de uma função com base em alguns pontos de dados.
> Dados são rotulados;
> Permite coletar dados e produzir saída de dados de experiências anteriores;
> Ajuda a otimizar os critérios de desemprenho com a ajuda da experiência;
> O aprendizado de máquina supervisionado ajuda a resolver vários tipos de problemas de computação do mundo real.

Algoritmos da Aprendizagem Supervisionada:
> KNN (K-ésimo Vizinho mais Próximo);
> Árvore de decisão;
> SVM (Support Vector Machine);
    Vantagens do SVM:
    > Tem um bom desempenho para conjunto de dados complicados;
    > Pode ser usado para um classificado multi-classe.
    Desvantagem do SVM:
    > Não terá um bom desempenho quando tiver um conjunto de dados muito grande porque leva muito tempo de treinamento.
    > Não funcionará bem quando os dados tiverem muito ruído.
> Naive Bayes;
    Por exemplo, uma fruta pode ser considerada uma maçã se for vermelha, redonda e tiver cerca de 7 centimetros
    de diâmetro. Mesmo que essas características dependam umas das outras, ou da existência de outras características,
    todas essas propriedades contribuem de forma independente para a probabilidade de que esta fruta seja uma maçã,
    e é por isso que é conhecida como 'Naive=Ingênua'.
> Regressão Logística;
    A regressão logística é a análise de regressão apropriada a ser conduzida quando a variável dependente
    é dicotômica (binária).
    Tipos de perguntas que a regressão logística binária pode responder:
    > Como a probabilidade de desenvolver câncer de pulmão (sim ou não) muda para cada quilo adicional que uma pessoa
    está acima do peso e para cada maço de cigarros fumado por dia?
    > O peso corporal, a ingestão de calorias, de gordura e a idade influenciam a probabilidade de sofrer um ataque
    cardíaco (sim ou não)?
"""

"""
NLP SUPERVISIONADA
Abordagens supervisionadas são atualmente as abordagens de fluxo de extração de relações com melhor desemprenho,
desde que uma quantidade suficiente de dados de treinamento rotulados esteja disponível.
Antes que os textos de entrada possam ser alimentados em classificadores, cada texto precisa ser transformado em um
conjunto de recursos.

BAG OF WORDS
A maneira mais simples de representar textos é usando o modelo Bag of Words (saco de palavras).
Os recursos linguísticos podem ser usados em adição ou em vez dos recursos baseados em palavras.

TREINAMENTO
Durante o treinamento, o modelo observa com que frequência um recurso ocorre simultaneamente com exemplos de treinamento
positivos em oposição a negativos e, com base nisso, aprende um pesa para cada recurso, que pode ser novamente
positivo ou negativo.

TIPOS DE DADOS
Uma questão importante em relação aos dados é que nem todos os tipos de dados são apropriados ao usar certos tipos de 
modelos. Os dados costumam ser confusos e difíceis de agregar.
Para formar um conjunto de treinamento ou teste, ou fornecer variáveis a um modelo para previsões, provavelmente
precisaremos lidar com vários formatos de dados, como CSV, JSON e tabelas de banco de dados.

TRATAMENTO DOS DADOS
As transformações comuns incluem:
> Análise de valor ausente;
> Análise de data e hora;
> Conversão de dados categóricos em dados numéricos;
> Normalização de valores;
> Aplicação de alguma função entre valores;

CONJUNTOS DE DADOS DE PLN
> Reconhecimento de fala: as palavras reais faladas em audio são convertidas em texto para análise posterior.
> Classificação de texto e modelagem de linguagem: fragmentação e classificação da fala em conceitos para análise
posterior.
> Legenda da imagem: texto adicionado para descrever uma fotografia.
> Resposta a perguntas: Gerando conversas de chatbot.
> Sumarização de documentos: condensar um trecho de texto em uma versão mais curta, preservando os principais elementos
informativos e o significado do conteúdo.

INTERAÇÃO COM DADOS
A interação com os dados é parte importante do processo de construção de um sistema de PLN.
"""

"""
APRENDIZADO SUPERVISIONADO
O aprendizado supervisionado é o que a maioria das pessoas entende quando pensa em aprendizado de máquina.
Nesse tipo de Machine Learning, fornecemos um conjunto de dados rotulado como entrada para o algoritmo de ML saber
o que é correto e o que não é correto.
> Por exemplo: suponha que temos alguns dados de texto com rótulos como e-mails de spam e e-mails não spam. Cada
fluxo de texto do conjunto de dados tem um desses dois rótulos.
> No aprendizado supervisionado, você receberá feedback após cada etapa ou previsão.

A abordagem geral de aprendizagem supervisionada consiste em cinco etapas:
    > Pré processamento linguístico;
    > Extração de características;
    > Modelos de treinamento em dados de treinamento;
    > aplicação de modelos para testar dados;
    > pós processamento dos resultados para marcar os documentos;

Os dados de treinamento contêm vetores de documentos para os quais as classes são fornecidas.
O classificador usa os dados de treinamento para aprender associações entre recursos ou combinações de recursos
fortemente associados a uma das classes, mas não às outras classes. Dessa forma, o modelo treinado pode fazer previsões
para dados de teste não vistos no futuro.
Normalmente, os modelos de aprendizado supervisionado requerem ciclos de otimização extensos e iterativos.
Esse tipo de aprendizagem mantém a palavra 'supervisionado' porque sua firma de aprender a partir dos dados de
treinamento imita o mesmo proceso de um professor supervisionando o processo de aprendizagem ponta a ponta.

> Ocupa bastante espaço e processamento com uso de recursos.
> Os conjuntos de dados podem ter uma probabilidade maior de erro humano, resultando em algoritmos aprendendo
incorretamente.
> Ao contrário dos modelos de aprendizagem não supervisionada, não pode agrupar ou classificar dados por conta própria.

SCIKIT-LEARN
É uma das bibliotecas mais populares do Python +ara fazer aprendizado de máquina supervisionado. Se integra muito bem
com a pilha SciPy, tornando-o robusto e poderoso.
O scikit-learn pode ser usado para problemas de classificação e regressão.
Algoritmos supervisionados prontos para o uso:
    > Modelos lineares;
    > Análise Discriminante Linear e Quadrática;
    > SVM;
    > KNN;
    > Naive Bayes;
    > Árvores de decisão;
    > Modelos de rede neural;
    
Documentação: https:// scikit-learn.org/stable/supervised_learning.html
"""

#Exemplo:
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)