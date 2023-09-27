from textblob import TextBlob
import time

def det_sentimiento(historia):
    historia_blob=TextBlob(historia)
    sentimientos=[]
    for frase in historia_blob.sentences:
        sentimiento=frase.sentiment
        for sp in sentimiento:
            sentimientos.append(sp)
       
        #print(f'{frase}')
        #print(f'Sentimiento: {frase.sentiment}')

    polaridad=[]
    subjetividad=[]
   
    for i in range(len(sentimientos)):
        if i % 2 ==0:
            polaridad.append(sentimientos[i])
        else:
            subjetividad.append(sentimientos[i])
    #print(f'La polaridad de cada frase es:\n{polaridad}\nLa subjetividad de cada frase es:\n {subjetividad}\n')
    #return polaridad, subjetividad

    #calculo de las medias de las listas de pys
    media_polaridad=medias_ps(polaridad)
    media_subj=medias_ps(subjetividad)

    polaridad_periodico=[]
    subjetividad_periodico=[]
    polaridad_periodico.append(media_polaridad)
    subjetividad_periodico.append(media_subj)

    #time.sleep(3)
    print('TEST FINAL')
    print(f'Nivel de subjetividad( de 0 a 1): {sentimiento_general(media_subj,"subjetividad" )}({media_subj})')
    print(f'Nivel polaridad de (-1 a 1):{sentimiento_general(media_subj,"polaridad")} ({media_polaridad})')
    return subjetividad_periodico,polaridad_periodico
def medias_ps(lista):
    resultado=sum(lista)/len(lista)    
    #print(resultado)
    return resultado

def sp_periodico(subjetividad_periodico,polaridad_periodico):
    
    media_p_total=sum(subjetividad_periodico)/len(subjetividad_periodico)
    media_s_total=sum(polaridad_periodico/len(polaridad_periodico))
    print(f'La subjetividad media del periodico es: {media_s_total}\nLa polaridad media del periodico es: {media_p_total}')
    return media_p_total,media_s_total


  



#polaridad,subjetividad= det_sentimiento(resumen)



def sentimiento_general(sentimiento,tipo):
    categoria=""
    if tipo == 'subjetividad':
        if sentimiento ==1:
           categoria= "Totalmente subjetivo"
        elif 0.99>=sentimiento >= 0.75:
           categoria='Altamente subjetivo'
        elif 0.75> sentimiento>=0.55:
            categoria= 'Subjetividad media-alta'
        elif  0.55> sentimiento>0.5:
            categoria='Ligeramente subjetivo'
        elif sentimiento==0.5:
            categoria='Nivel moderado de objetividad media'
        elif 0.5>sentimiento>=0.45:
            categoria='Ligeramente objetivo'
        elif 0.45> sentimiento>=0.35:
            categoria= 'Objetividad media-alta'
        elif 0.35>sentimiento>=0.01:
            categoria= 'Altamente objetivo'
        elif sentimiento ==0:
            categoria= 'Totalmente objetivo'
        else:
            print('Input invalido')
        return categoria
    elif tipo=='polaridad':
        categoria=""
        if sentimiento==1:
            categoria='Vision radicalmente positiva'
        elif 0.99>=sentimiento>=0.5:
            categoria='Vision predominantemente positiva'
        elif 0.5>sentimiento>0:
            categoria='Vision ligeramente positiva'
        elif sentimiento ==0:
            categoria='Perspectiva neutra'
        elif 0>sentimiento>=-0.5:
            categoria='Perspectiva ligeramente negativa'
        elif -0.5>sentimiento>=-0.99:
            categoria='Vision predominantemente negativa'
        elif sentimiento ==-1:
            categoria='Vision radicalmente negativa'
        return categoria


#det_sentimiento(resumen)
