import time
from extraccion import *
from scraping import *
from noticias_nlp import *
from washington_post.extraccion_wp import WashingtonPost,ElMundo


def procesar_nyt(url):

        
    print('Extrayendo los hiperenlaces de las ultimas noticias...')
    print(url)
    time.sleep(2)
    contenido_interes=get_contenido(url)
    primeros_indices,final_indices,url=parseo_contenido(contenido_interes,url)
    urls_limpias=get_urls(primeros_indices, final_indices,contenido_interes,url)
    #llamando resumen
    # def llamar_resumen(urls_limpias):
    for i in urls_limpias:
        print('-----------')
        print(urls_limpias)
        print(f'La URL del articulo es: {i}\n')
        resumen=coger_noticias(i)
        print('---------------')
        det_sentimiento(resumen)
        print('.......')
    return contenido_interes,urls_limpias,url
    #return npl

        
def procesar_wp(url):
    urls_wp=washingtonPost.extraccion_wp(url)
    for i in urls_wp:
        print('-----------')
        #print(urls_wp)
        print(f'La URL del articulo es: {i}\n')
        resumen=coger_noticias(i)
        print('---------------')
        det_sentimiento(resumen)
        print('.......')
    return url,urls_wp


def procesar_elMundo(url):
    urls=elMundo.extraccion_em(url)
    print(urls)

    return url,urls


washingtonPost=WashingtonPost()
elMundo=ElMundo()