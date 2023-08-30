# PROCESSAMENTO DE LINGUAGEM NATURAL

# Modelos de Aprendizagem
"""Os modelos de aprendizagem devem ser capazes de compreender a linguagem humana com todas as suas especificidades
e nuances
"""

# Sistema de PLN
"""
CONCEITOS LINGUÍSTICOS:
> Verbo
> Substantivo
> Adjetivo

ESTRUTURA GRAMATICAL:
> Frases
> Locuções
> Relações de dependência
"""

"""
TEORIAS GRAMATICAIS:
Conjuntos de principios
Sistemas de restrições
Conjuntos de representações
Dicionário de palavras
"""

# Fragmentos de Linguagem
"""
> Uma Palavra;
> Uma frase incompleta;
> Linguagem falada;
"""

# Pipeline de Pré-processamento linguístico
"""
TOKENIZAÇÃO:
Contexto    :   Hoje o dia está lindo, acho que não vai chover.
Token       :   |Hoje|o|dia|está|lindo|,|acho|que|não|vai|chover|.|

DIVISÃO DE SENTENÇAS:
Texto
> Texto Original
> Artigo de jornal
> Parágrafo
> Frase
> Palavra

MARCAÇÃO DE PARTE DO DISCURSO
Tags POS universais
> ADJ: adjetivo
> ADP: adposição
> ADV: advérbio
> AUX: verbo auxiliar
> CONJ: conjunção ordenadora
> DET: determiner
> INTJ: interjeição
> NOUN: substantivo
> NUM: numeral
> PARTE: partícula
> PRON: pronome
> PROPN: pronome próprio
> PUNCT: pontuação
> SCONJ: conjunção subordinada
> SYM: símbolo
> VERBO: verbo
> X: outro

ANÁLISE MORFOLÓGICA
A análise morfológica diz respeito essencialmente à identificação e classificação das unidades linguísticas de uma
palavra, normalmente dividindo a palavra em sua forma de raiz e um afixo.

ANÁLISE E FRAGMENTAÇÃO
A análise sintática preocupa-se com a análise de sentenças para derivar sua estrutura sintática de acordo com uma
gramática. Essencialmente, a análise explica como os diferentes elementos de uma frase estão relacionados entre si, por
exemplo, como o sujeito e o objeto de um verbo estão conectados.
"""

# PARTICIONANDO UMA LINGUAGEM
"""
TONKENIZAÇÃO
A tokenização ou segmentação é uma etapa necessária em quase todos os aplicativos de processamento linguístico.
A tokenização é uma forma de separar um pedaço de texto em unidades menores chamadas tokens.

Palavras > Caracteres > Sub-palavras

A maneira mais simples de tokenizar uma frase é usar um espaço em branco dentro de uma string como o 'delimitador'
de palavras.

Pontuação Pura > Pontuação de Palavras > Pontuação a Ignorar

STOPWORDS
são palavras comuns em qualquer idioma que ocorrem com alta frequência, mas contêm informações muito menos substantivas
sobre o significado de uma frase. Exemplos: um, uma, a, isto, e, ou, do, de.

> Depende da aplicação específica;
> Tamanho do vocabulário (complexidade computacional, requisitos de CPU e memória)
> Não há uma lista única de stopwords disponível universalmente e elas variam principalmente com base nos casos de uso.
> O pacote NLTK tem suporte de stopwords para vários idiomas.
> Também podemos compilar uma lista de stopwords usando o texto con o qual estamos trabalhando e calculando a
frequência das palavras nele.
"""

# NORMALIZAÇÃO
"""
Outra técnica de redução de vocabulário é normalizar seu vocabulário para que tokens que significam coisas semelhantes
sejam combinados em uma única forma normalizada.

A normalização:
> Reduz o número de tonkes;
> Melhora a associação de significado;
> Diminui o Overfitting
"""

# DOBRADURA DE MAIÚSCILAS
"""
> Consolida várias 'grafias' de uma palavra que diferem apenas em sua capitalização;
> Consolida palavraque que têm o mesmo significado;
> Reduz o tamanho do vocabulário;

Frequentemente, a capitalização é usada para indicar que uma palavra é um substantivo próprio, o nome de uma pessoa,
lugar ou coisa.
"""

# ABORDAGENS
"""
> Reduzir o tamanho do vocabulário (dependendo da aplicação);
> Testar várias abordagens (dependendo da área de aplicação do PLN);
"""