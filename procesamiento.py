import time
from extracciones.extraccion_nyt import *
from scraping import *
from npl.noticias_nlp import *
from extracciones.extraccion_varias import WashingtonPost,ElMundo
from bbdd.create_db import insercion_datos


def procesar_nyt(url,conn,cursor,seccion):

    #subjetividad_periodico=[]   
    print('Extrayendo los hiperenlaces de las ultimas noticias...')
    print(url)
    nombre_medio='New York Times'
    tipo_medio='periodico'
    #time.sleep(2)
    contenido_interes=get_contenido(url)
    primeros_indices,final_indices,url=parseo_contenido(contenido_interes,url)
    urls_limpias=get_urls(primeros_indices, final_indices,contenido_interes,url)
    #llamando resumen
    # def llamar_resumen(urls_limpias):
    for i in urls_limpias:
        print('-----------')
        #print(urls_limpias)
        print(f'La URL del articulo es: {i}\n')
        titulo_noticia,fecha_publicacion,autor,resumen,texto,keywords,imagen_principal,imagenes_2=coger_noticias(i)
        print('---------------')
        media_polaridad,media_subjetividad=det_sentimiento(texto)
       #media_polaridad,media_subjetividad=det_sentimiento(i,titulo_noticia,fecha_publicacion,resumen,texto,keywords,im_principal,imagenes_2)
        insercion_datos(conn,cursor,nombre_medio,tipo_medio,i,seccion,titulo_noticia,fecha_publicacion,autor,resumen,texto,keywords
,media_subjetividad,media_polaridad,imagen_principal,imagenes_2)
        print('.......')

    #insercion_datos(conn,cursor)
    print('todo correcto')
    #return contenido_interes,urls_limpias,url,nombre_medio,tipo_medio
    return url, nombre_medio
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
   print('Contenido extraido')
   for i in urls:
        print(f'La URL del articulo es: {i}\n')
        texto=coger_noticias(i)
        print('---------------')
        det_sentimiento(texto)
        print('.......')     
   return url,urls


def procesar_elDiario(url):
    urls=elMundo.extraccion_em(url)
    print('Contenido extraido')
    scraping_elDiario(urls)
    print('fin scraping')
    """for i in urls:
            print(f'La URL del articulo es: {i}\n')
            texto=coger_noticias(i)
            print('---------------')
            det_sentimiento(texto)
            print('.......')    """ 
    return url,urls

    #fechas=scraping_elDiario(urls)
    #return fechas,urls
   

washingtonPost=WashingtonPost()
elMundo=ElMundo()