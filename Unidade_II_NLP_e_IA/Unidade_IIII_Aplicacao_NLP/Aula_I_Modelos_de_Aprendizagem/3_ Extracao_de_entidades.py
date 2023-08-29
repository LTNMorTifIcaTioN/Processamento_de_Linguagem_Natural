import spacy
#python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")
text = """Fernando viajou de MG para SP para visitar o MASP. Depois foi visitar a sede da Petrobrás no
        Rio de Janeiro."""
document = nlp(text)
for ent in document.ents:
    print(ent.text, '=', ent.label_)

# import spacy
# from spacy.lang.pt.examples import sentences
#
# nlp = spacy.load("pt_core_news_sm")
# doc = nlp(sentences[0])
# print(doc.text)
# for token in doc:
#     print(token.text, token.pos_, token.dep_)