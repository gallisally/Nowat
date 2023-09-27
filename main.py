#from demo_npl import *
"""from menu import *
from extraccion import *
from scraping import *"""


from menu import Menus
from extracciones.extraccion_nyt import get_contenido, parseo_contenido, get_urls
from scraping import *
import time


#from main_prueba import *
from npl.noticias_nlp import *
#from washington_post import seccion_wp,menu_wp

import time

def inicio():
    menus=Menus()
    url=menus.menu_principal()
    
    #menu_principal()
    return url





menus=Menus()

url=inicio()
"""
url=inicio()
urls_limpias,contenido_interes,url =llamar_extraccion(url)
i,resumen=llamar_resumen(urls_limpias)
"""

#INSTANCIAS


#seccion=Seccion()

