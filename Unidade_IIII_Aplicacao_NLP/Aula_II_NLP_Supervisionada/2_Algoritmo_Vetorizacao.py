# BAG OF WORDS
from keras.preprocessing.text import Tokenizer

doc = [
    'O menino correu',
    'O menino correu para dentro',
    'O menino correu para dentro de casa',
]

# Determinando o vocabulário
tokenizer = Tokenizer()
tokenizer.fit_on_texts(doc)
print(f'Vocabulary: {list(tokenizer.word_index.keys())}')

# Contando palavras
vectors = tokenizer.texts_to_matrix(doc, mode='count')
print(vectors)