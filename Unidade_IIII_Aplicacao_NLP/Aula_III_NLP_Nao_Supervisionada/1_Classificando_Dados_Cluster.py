# Carregando bibliotecas

#pip install wikipedia
import pandas as pd
import wikipedia
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from wordcloud import WordCloud

# Selecionando conteúdo dos artigos

articles = [
    'Petrobras', 'Companhia Siderurgica Nacional', 'Usiminas', 'Banco Itau Unibanco', 'Gerdau', 'Eletrobras',
    'AMBEV', 'Cemig', 'CPFL Energia', 'ArcelorMittalc', 'Banco do Brasil', 'Friboi'
]


# Armazenando o conteúdo de cada artigo em uma lista

wiki_lst = []


# Armazenando o titulo de cada artigo na variável title

title = []
for article in articles:
    print("Carregando conteúdo do artigo: ", article)
    wiki_lst.append(wikipedia.page(article).content)
    title.append(article)


# Transformando cada artigo em um vetor

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(wiki_lst)


# Agrupamento K-Means

Sum_of_squared_distances = []
K = range(2, 12)
for k in K:
    km = KMeans(n_clusters=k, max_iter=200, n_init=10)
    km.fit(X)
    Sum_of_squared_distances.append(km.inertia_)


# Plotando o gráfico

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Soma das distâncias ao quadrado')
plt.title('Método do cotovelo para k ideal')
plt.show()


# Definindo a quantidade de clusters

true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=2000, n_init=10)
model.fit(X)
labels = model.labels_
wiki_cl = pd.DataFrame(list(zip(title, labels)), columns=['Titulo', 'cluster'])

print()
print(wiki_cl.sort_values(by=['cluster']))

# Avaliando o Resultado

result = {'cluster':labels, 'wiki':wiki_lst}
result=pd.DataFrame(result)
for k in range(0, true_k):
    s = result[result.cluster == k]
    text = s['wiki'].str.cat(sep=' ')
    text = text.lower()
    text = ' '.join([word for word in text.split()])

    # Criando uma nuvem de palavras com 50 palavras
    wordcloud = WordCloud(max_font_size=50, max_words=50, background_color="white").generate(text)
    print('Cluster: {}'.format(k))
    print('Titulo')
    titles=wiki_cl[wiki_cl.cluster == k]['Titulo']
    print(titles.to_string(index = False))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()