# Uso da biblioteca NLTK para remoção de stops words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('portuguese')
print(stop)