
#import nltk
#nltk.download('wordnet')

# Download window opens, fetch wordnet
#from nltk.corpus import wordnet as wn
from textblob import TextBlob,Word
import random2


resumen= '''It looks like somebody took a bunch of dynamite and threw it up on top of the trees,” he said.
The hurricane made landfall on Wednesday in a sparsely populated area of Florida known as the Big Bend, which includes Levy County.
Mr. Bobbitt, 47, knew that Cedar Key’s mayor had begged people to leave on Tuesday.
“I felt like I had some resources here to be able to help folks,” Mr. Bobbitt said.
“Our little downtown shopping district, with our restaurants and our shops — 100 percent of those buildings are ruined,” Mr. Bobbitt said.'''

def clasificacion_texto(texto):
    print('Resumen:'+ '\n'+ texto)
    print()
    print('---------')
    resumen=TextBlob(texto)

    #POS TAGGING
    print(f'Etiquetado de palabras(POS):\n {resumen.tags}')
    print()
    #WORD TOKENIZATION
    print(f'Palabras:\n {resumen.words}')
    print()
    #WORDS INFLECTION
    print(f'Plurales:\n {resumen.words[8]}: {resumen.words[8].pluralize()}\n')
    #SENTENCE TOKENIZATION
    print(f'Frases\n: {resumen.sentences}\n')
    #DYNAMIC SUMMARY GENERATOR
    sustantivos=[]
    for palabra,etiqueta in resumen.tags:
        if etiqueta=='NN':
            sustantivos.append(palabra)
    print(f'Los sustantivos son:\n {sustantivos} \n')

    print('Este texto trata sobre:')
    for i in random2.sample(sustantivos,5):
        #creando objeto
        palabras_clave=Word(i)
        #find dictionnary base origins of a word
       
        palabras_clave=palabras_clave.lemmatize()
        print(palabras_clave.pluralize())

clasificacion_texto(resumen)