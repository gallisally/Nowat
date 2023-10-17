import time
from extracciones.extraccion_nyt import *
from scraping import *
from npl.noticias_nlp import *
from extracciones.extraccion_nyt import *
from extracciones.extraccion_varias import WashingtonPost,ElMundo
from bbdd.create_db import insercion_datos
from menu import *


def procesar_guardar_periodico(secciones,conn,cursor,nombre_medio,tipo_medio):
    for seccion, url_seccion in secciones:
                    print(f'Procesando seccion: {seccion}')
                    url = url_seccion
                    print(f'La url de la seccion es : {url}') 
                    urls=funcion_extraccion(nombre_medio,url) 
                    scraping_sentimientos(urls,conn,cursor,nombre_medio,tipo_medio,seccion)
                
def scraping_sentimientos(urls,conn,cursor,nombre_medio,tipo_medio,seccion):     
      for url in urls:
        #print(urls_limpias)
        print(f'La URL del articulo es: {url}\n')  
        
        titulo_noticia,autor,fecha_publicacion,resumen,texto,keywords,imagen_principal,imagenes_2=coger_noticias(url)
        """if titulo_noticia=='' and fecha_publicacion==None and resumen=='' and texto=='':
              pass
        else:
        """
        print('se han cogido las noticias')
        print('---------------------------------------------------')
        if texto=='': 
          media_polaridad=None
          media_subjetividad=None
        else:        
          media_polaridad,media_subjetividad=det_sentimiento(texto)
          return media_subjetividad,media_polaridad
        #print(url)

        insercion_datos(conn,cursor,nombre_medio,tipo_medio,url,seccion,titulo_noticia,autor,fecha_publicacion,resumen,texto,keywords
                ,media_subjetividad,media_polaridad,imagen_principal,imagenes_2)
        #print(f'{seccion} procesada')
        print(f'la urlmetida es {url}')
        print(f'el titulo a mater es: {titulo_noticia}')
        print(f'autor metido es_{autor}')
        print(f'fecha metida :{fecha_publicacion}')
      #return titulo_noticia,autor,fecha_publicacion,resumen,texto,keywords,media_polaridad,media_subjetividad,imagen_principal,imagenes_2
      


washingtonPost=WashingtonPost()
elMundo=ElMundo()