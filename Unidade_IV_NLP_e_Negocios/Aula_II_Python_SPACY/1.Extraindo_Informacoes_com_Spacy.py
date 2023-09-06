import spacy
texto = input('Digite um texto: ')
nlp = spacy.load('pt_core_news_sm')
doc = nlp(texto)
print(doc.text.split())
print([token.orth_ for token in doc if not token.is_punct])
print('==============================================================================================================')


print([(token.orth_, token.pos_) for token in doc])
print([token.lemma_ for token in doc if token.pos_=='VERB'])
print(doc.ents)
print([(entity, entity.label_) for entity in doc.ents])
for frase in doc.sents:
    print(frase)