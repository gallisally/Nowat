#from demo_npl import *

from extraccion import *
from scraping import *

#from main_prueba import *
from noticias_nlp import *

import time

def inicio():
    print('Bienvenido a NOWATT, una app donde puedes acceder a diferentes periodicos sin necesidad de suscripcion y comparar los contenidos de sus publicaciones.\n Gracias a ella podrás investigar como un mismo tema es tratado desde diferentes persectivas y conseguir así formarte una opinion lo más completa posible sobre los sucesos actuales que son de interes público.')
    nombre=input('Para poder ofrecerte una atención más personalizada, introduce, por favor, tu nombre:')
    print(f'{nombre}, Bienvenido/a a Nowatt. Hora de empezar a analizar noticias\n')
    time.sleep(2)
    return nombre

def llamar_extraccion():
    print('Extrayendo los hiperenlaces de las ultimas noticias...')
    time.sleep(2)
    contenido_interes = get_contenido('https://www.nytimes.com/section/technology')
    #parseo_contenido(contenido_interes)
    primeros_indices,final_indices=parseo_contenido(contenido_interes)
    urls=get_urls(primeros_indices, final_indices,contenido_interes)
    return urls

def llamar_resumen():
    for url in urls_limpias:
        print(f'La URL del articulo es: {url}\n')
        resumen=coger_noticias(url)
        print('---------------')
        det_sentimiento(resumen)
        print('.......')
        #return npl
        
        


llamada=inicio()
urls_limpias =llamar_extraccion()
todo=llamar_resumen()

