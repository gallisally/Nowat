#from demo_npl import *
"""from menu import *
from extraccion import *
from scraping import *"""


from menu import Menus
from extraccion import get_contenido, parseo_contenido, get_urls
from scraping import *
import time


#from main_prueba import *
from noticias_nlp import *
#from washington_post import seccion_wp,menu_wp

import time

def inicio():
    menus=Menus()
    url=menus.menu_principal()
    
    #menu_principal()
    return url
"""
def procesar_nyt():

    

    def llamar_extraccion(url):
        print('Extrayendo los hiperenlaces de las ultimas noticias...')
        print(url)
        time.sleep(2)
        contenido_interes=get_contenido(url)
        primeros_indices,final_indices,url=parseo_contenido(contenido_interes,url)
        urls_limpias=get_urls(primeros_indices, final_indices,contenido_interes,url)
        return urls_limpias,url,contenido_interes

    def llamar_resumen(urls_limpias):

        for i in urls_limpias:
            print('-----------')
            print(urls_limpias)
            print(f'La URL del articulo es: {i}\n')
            resumen=coger_noticias(i)
            print('---------------')
            det_sentimiento(resumen)
            print('.......')
            #return npl
        return i,resumen
    return llamar_extraccion,llamar_resumen
    """
        
menus=Menus()


url=inicio()
"""
url=inicio()
urls_limpias,contenido_interes,url =llamar_extraccion(url)
i,resumen=llamar_resumen(urls_limpias)
"""

#INSTANCIAS


#seccion=Seccion()

