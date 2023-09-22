import time
from extraccion import *
from procesamiento import procesar_nyt,procesar_wp,procesar_elMundo
from washington_post.extraccion_wp import WashingtonPost,ElMundo
#from extraccion import llamar_extraccion,llamar_resumen
#from  washington_post.extraccion_wp import WashingtonPost
#from washington_post import extraccion_wp 

class Menus:
    def __init__(self):
        self.nombre=""

    def menu_principal(self):

        while True:
            print('Bienvenido a NOWATT, una app donde puedes acceder a diferentes periodicos sin necesidad de suscripcion y comparar los contenidos de sus publicaciones.\n Gracias a ella podrás investigar como un mismo tema es tratado desde diferentes persectivas y conseguir así formarte una opinion lo más completa posible sobre los sucesos actuales que son de interes público.')
            nombre=input('Para poder ofrecerte una atención más personalizada, introduce, por favor, tu nombre:')
            print(f'{nombre}, Bienvenido/a a Nowatt. Hora de empezar a analizar noticias\n')
            time.sleep(2)
            menu_1=f"""{nombre}¿En que periodico deseas entrar?\n Elige uno de los siguientes:
            1- NEW YORK TIMES
            2- WASHINGTON POST
            3- EL MUNDO
            4- EL PAIS
            5- LIBERTAD DIGITAL
            6- EL CONFIDENCIAL"""

            eleccion=input(menu_1)
            seccion =Seccion()
            if eleccion =='1':
                
                print('Has elegido el New York Times')
                url=seccion.nyt_menu(self.nombre)
                procesado=procesar_nyt(url)
                return url,procesado
            elif eleccion =='2':
                print('Has elegido el Washington Post')
                url=seccion.menu_wp(self.nombre)
                procesado=procesar_wp(url)
                print('------')
                #seccion.nyt_menu(nombre)
                return url,procesado
                #return eleccion
            elif eleccion=='3':
                print('Has elegido el perodico El Mundo')
                url='https://www.elmundo.es/index.html?utm_source=google&utm_medium=cpc&utm_campaign=unidadeditorial_elmundo_cpc_performance_HMG&utm_content=elmundo__&gad=1&gclid=Cj0KCQjw9rSoBhCiARIsAFOiplkQUuciuxX4E2LstYclP6sGEq_P8hFU4t24M1Djx7rzrYqGKFd_nKoaAtg7EALw_wcB'
                procesado=procesar_elMundo(url)
                return url,procesado
            else:
                print('Esta opcion aun no esta configurada')
                break
            
            
        
    

class Seccion:
    def __init__(self):
        self.seccion=""
        self.url=""
    
    def nyt_menu(self,nombre):

        while True:
            seccion=f"""{nombre}¿Que seccion del periodico deseas procesar?')
            1- Portada del dia
            2- Politica
            3- Salud
            4- Negocios
            5- Opinion
            6- Tecnologia"""
            eleccion=input(seccion)
            url=""

           
            if eleccion=='1':
                print('Procesando portada del NYT')
                url=self.url="https://www.nytimes.com/"
                
                return url
                
            elif eleccion=='2':
                print('Abriendo seccion politica del NYT')
                url=self.url=('https://www.nytimes.com/section/politics')
                
            elif eleccion=='3':
                print('Abriendo seccion Salud del NYT')
                url=self.url='https://www.nytimes.com/section/health'
            elif eleccion=='4':
                print('Abriendo seccion de Negocios del NYT')
                url=self.url='https://www.nytimes.com/section/business'
            elif eleccion =='5':
                print('Abriendo seccion Opinion del NYT')
                url=self.url='https://www.nytimes.com/section/opinion'
            elif eleccion=='6':
                print('Abriendo seccion de Tecnologia del NYT')
                url=self.url='https://www.nytimes.com/section/technology'
            else:
                print('Esta opcion aun no esta programada. Por favor, mete la opcion correcta')   
            return url
        
    def menu_wp(self,nombre):

        while True:
            seccion=f"""{nombre}¿Que seccion del periodico deseas procesar?')
            1- Portada del dia
            2- Politica
            3- Opinion
            4- Guerra Rusia-Ucrania
            5- Estilo
            6- Investigaciones
            7- Clima y Medio Ambiente
            8- Bienestar
            9- Tecnologia
            10- Mundo general
            """
            eleccion=input(seccion)
            url=""

            
            if eleccion=='1':
                print('Procesando portada del Washington Post')
                url=self.url="https://www.washingtonpost.com/"
                return url
                
            elif eleccion=='2':
                print('Abriendo seccion politica del Washington Post')
                url=self.url=('https://www.washingtonpost.com/politics/')
            elif eleccion=='3':
                print('Abriendo seccion Opinion en el Washington Post')
                url=self.url='https://www.washingtonpost.com/opinions/'
            elif eleccion=='4':
                print('Abriendo seccion de Guerra Rusia-Ucrania en el Washington Post')
                url=self.url='https://www.washingtonpost.com/world/ukraine-russia/'
            elif eleccion =='5':
                print('Abriendo seccion Estilo de Washington Post')
                url=self.url='https://www.washingtonpost.com/style/'
            elif eleccion=='6':
                print('Abriendo seccion de Investigaciones de Washington Post')
                url=self.url='https://www.washingtonpost.com/national/investigations/'

            elif eleccion=='7':
                print('Abriendo seccion sobre el Clima y el Cambio Climatico')
                url=self.url='https://www.washingtonpost.com/climate-environment/'
            elif eleccion =='8':
                print('Abriendo seccionde Bienestar')
                url=self.url='https://www.washingtonpost.com/wellbeing/'
            elif eleccion=='9':
                print('Abriendo seccion de Tecnologia')
                url=self.url='https://www.washingtonpost.com/business/technology/'
            elif eleccion=='10':
                print('Abriendo seccion sobre el mundo ')
                url=self.url('https://www.washingtonpost.com/world/')
            else:
                print('Esta opcion aun no esta programada. Por favor, mete la opcion correcta')
            
        
            return url

washingtonPost=WashingtonPost()
elMundo=ElMundo()
#menus=Menus()
#seccion =Seccion()
#seccion_wp=Seccion_wp()
#washingtonPost=WashingtonPost()
