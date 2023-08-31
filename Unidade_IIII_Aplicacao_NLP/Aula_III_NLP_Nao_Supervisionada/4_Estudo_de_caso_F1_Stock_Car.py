# Instalando e importando bibliotecas

#pip install feedparser
import nltk
import random
import feedparser
nltk.download('stopwords')


# Definindo os dois feeds de RSS que serão utilizados
urls = {
    'Motor': 'https://ge.globo.com/Esportes/Rss/0,,AS0-15010,00.xml',
    'Brasileirao': 'https://ge.globo.com/Esportes/Rss/0,,AS0-9825,00.xml',
}


# Inicializando o feedmap de variável de dicionário vazio para manter a lista de feeds RSS na memória
feedmap = {}


# Obtendo as stopwords em português
stopwords = nltk.corpus.stopwords.words('portuguese')


# Adiciona lista de palavras ao dicionário
def featureExtractor(words):
    features = {}
    for word in words:
        if word not in stopwords:
            features[f'word({word})'] = True
    return features


# Cria uma lista vazia para armazenar as frases rotuladas corretamente
sentences = []


# Armazena as chaves das variáveis
for category in urls.keys():
    # Download do feed e armazenamento do mesmo na variavel feedmap
    feedmap[category] = feedparser.parse(urls[category])
    # Imprimindo a url
    print(f'downloading {urls[category]}')
    # Repita todas as entradas RSS e armazene a entrada atual em uma variável de entrada
    for entry in feedmap[category]['entries']:
        # Pega o resumo do feed RSS
        data = entry['summary']
        # Separação das palavras
        words = data.split()
        # Armazenar todas as palavras do feed atual junto a categoria a que pertencem
        sentences.append((category, words))


# Extraíndo e armazenando os recursos de frases
featuresets = [(featureExtractor(words), category) for category, words in sentences]
random.shuffle(featuresets)

# Criando datasetes (treinamento e testes)
total = len(featuresets)
off = int(total/2)
trainset = featuresets[off:]
testset = featuresets[:off]


# Criando o classificador
classifier = nltk.NaiveBayesClassifier.train(trainset)


# Imprimindo a precisão do classificador com o dataset de teste
print(nltk.classify.accuracy(classifier, testset))


# Imprimindo os recursos informativos sobre os dados
classifier.show_most_informative_features(8)


# Pegando amostras do RSS da Stock Car
for (i, entry) in enumerate(feedmap['Motor']['entries']):
    if i < 10:
        features = featureExtractor(entry['title']. split())
        category = classifier.classify(features)
        # Imprimindo os recursos mais informativos
        print()
        print(f'{category} -> {entry["summary"]}')