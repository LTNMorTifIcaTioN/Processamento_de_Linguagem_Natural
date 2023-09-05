import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string

texto = input('Digite um texto: ')
texto = texto.lower()
texto_pontuacao = "".join([p for p in texto if p not in string.punctuation])
print(texto)
tokenizacao = nltk.word_tokenize(texto_pontuacao)
print(tokenizacao)
nltk.download('stopwords')
stopwords = stopwords.words('portuguese')
palavras_stop = [p for p in tokenizacao if p not in stopwords]
print(stopwords)
print(palavras_stop)
freq = FreqDist(palavras_stop)
freq = freq.most_common(10)
print(freq)

# import nltk
# from nltk.corpus import stopwords
# from nltk.probability import FreqDist
# import string
#
# def preprocess_text(text):
#     text = text.lower()
#     text_without_punctuation = "".join([p for p in text if p not in string.punctuation])
#     return text_without_punctuation
#
# def remove_stopwords(tokenized_text):
#     stop_words = stopwords.words('portuguese')
#     words_without_stopwords = [word for word in tokenized_text if word not in stop_words]
#     return words_without_stopwords
#
# def get_most_common_words(words, n=10):
#     freq_dist = FreqDist(words)
#     most_common_words = freq_dist.most_common(n)
#     return most_common_words
#
# def main():
#     nltk.download('stopwords')
#     text = input('Digite um texto: ')
#     preprocessed_text = preprocess_text(text)
#     print(preprocessed_text)
#
#     tokenized_text = nltk.word_tokenize(preprocessed_text)
#     print(tokenized_text)
#
#     words_without_stopwords = remove_stopwords(tokenized_text)
#     print(words_without_stopwords)
#
#     most_common_words = get_most_common_words(words_without_stopwords)
#     print(most_common_words)
#
# if __name__ == "__main__":
#     main()