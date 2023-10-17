from textblob import TextBlob
import time
from extracciones.extraccion_varias import *

def det_sentimiento(historia):
    historia_blob = TextBlob(historia)
    polaridad = []
    subjetividad = []
    if not historia:
        media_subjetividad=None
        media_polaridad=None
        print('El texto es nulo')
    else:


        for frase in historia_blob.sentences:
            sentimiento = frase.sentiment
            polaridad.append(sentimiento.polarity)
            subjetividad.append(sentimiento.subjectivity)

        # Calculo de las medias de las listas de polaridad y subjetividad
        media_polaridad = medias_ps(polaridad)
        media_subjetividad = medias_ps(subjetividad)

    print('TEST FINAL')
    print(f'Nivel de subjetividad (de 0 a 1): {sentimiento_general(media_subjetividad, "subjetividad")} ({media_subjetividad})')
    print(f'Nivel polaridad (de -1 a 1): {sentimiento_general(media_polaridad, "polaridad")} ({media_polaridad})')
    return media_polaridad,media_subjetividad

def medias_ps(lista):
    if len(lista)>0:
        resultado = sum(lista) / len(lista)
    else:
        resultado=None
    return resultado

def sentimiento_general(sentimiento, tipo):
    categoria = ""
    if tipo == 'subjetividad':
        if sentimiento == 1:
            categoria = "Totalmente subjetivo"
        elif 0.99 >= sentimiento >= 0.75:
            categoria = 'Altamente subjetivo'
        elif 0.75 > sentimiento >= 0.55:
            categoria = 'Subjetividad media-alta'
        elif 0.55 > sentimiento > 0.5:
            categoria = 'Ligeramente subjetivo'
        elif sentimiento == 0.5:
            categoria = 'Nivel moderado de objetividad media'
        elif 0.5 > sentimiento >= 0.45:
            categoria = 'Ligeramente objetivo'
        elif 0.45 > sentimiento >= 0.35:
            categoria = 'Objetividad media-alta'
        elif 0.35 > sentimiento >= 0.01:
            categoria = 'Altamente objetivo'
        elif sentimiento == 0:
            categoria = 'Totalmente objetivo'
        elif sentimiento == 'null':
            categoria='Nulo'
        else:
            print('Input invalido')
        return categoria
    elif tipo == 'polaridad':
        categoria = ""
        if sentimiento == 1:
            categoria = 'Vision radicalmente positiva'
        elif 0.99 >= sentimiento >= 0.5:
            categoria = 'Vision predominantemente positiva'
        elif 0.5 > sentimiento > 0:
            categoria = 'Vision ligeramente positiva'
        elif sentimiento == 0:
            categoria = 'Perspectiva neutra'
        elif 0 > sentimiento >= -0.5:
            categoria = 'Perspectiva ligeramente negativa'
        elif -0.5 > sentimiento >= -0.99:
            categoria = 'Vision predominantemente negativa'
        elif sentimiento == -1:
            categoria = 'Vision radicalmente negativa'
        return categoria
