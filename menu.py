import time
from extracciones.extraccion_nyt import *
from procesamiento import procesar_nyt,procesar_wp,procesar_elMundo,procesar_elDiario
from extracciones.extraccion_varias import WashingtonPost,ElMundo
from npl.noticias_nlp import sp_periodico
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
            #time.sleep(2)
            menu_1=f"""{nombre}¿En que periodico deseas entrar?\n Elige uno de los siguientes:
            1- NEW YORK TIMES
            2- WASHINGTON POST
            3- EL MUNDO
            4- EL PAIS
            5- EL DIARIO
            6- EL CONFIDENCIAL"""

            eleccion=input(menu_1)
            seccion =Seccion()
            if eleccion =='1':
                
                print('Has elegido el New York Times')
                url=seccion.nyt_menu(self.nombre)
                procesado,subjetividad_periodico,polaridad_periodico=procesar_nyt(url)
                sp_periodico(subjetividad_periodico,polaridad_periodico)
                #return url,procesado
            elif eleccion =='2':
                print('Has elegido el Washington Post')
                url=seccion.menu_wp(self.nombre)
                procesado=procesar_wp(url)
                print('------')
                #seccion.nyt_menu(nombre)
                
                #return eleccion
            elif eleccion=='3':
                print('Has elegido el perodico El Mundo')
                url=seccion.menu_elMundo(self.nombre)
                procesado=procesar_elMundo(url)
                return url,procesado
            
            elif eleccion=='4':
                print('Abriendo El Pais')
                url=seccion.menu_elPais(self.nombre)
                procesado=procesar_elMundo(url)
                return url,procesado
            elif eleccion =='5':
                print('Abriendo elDiario.es')
                url=seccion.menu_elDiario(self.nombre)
                procesado=procesar_elDiario(url)
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
        

    def menu_elMundo(self,nombre):
        seccion=f"""{nombre}, has alegido El Mundo. ¿Que seccion quieres ver?
        1-Portada
        2-Opinion
        3-Economia
        4-Deportes
        5-Ciencia y Salud
        6-Internacional
        7-España"""
        url=""

        eleccion=input(seccion)

        if eleccion=='1':
            print('Procesando seccion Portada')
            url=self.url='https://e00-elmundo.uecdn.es/rss/portada.xml'
            return url
        elif eleccion =='2':
            print('Procesando seccion Opinion')
            url=self.url='https://e00-elmundo.uecdn.es/rss/opinion.xml'
        elif eleccion =='3':
            print('Procesando seccion Economia')
            url=self.url='https://e00-elmundo.uecdn.es/rss/economia.xml'
        elif eleccion =='4':
            print('Procesando seccion Deportes')
            url=self.url='https://e00-elmundo.uecdn.es/rss/deportes.xml'
        elif eleccion =='5':
            print('Procesando seccion Ciencia y salud')
            url=self.url='https://e00-elmundo.uecdn.es/rss/ciencia-y-salud.xml'
        elif eleccion =='6':
            print('Procesando la seccion Internacional')
            url=self.utl='https://e00-elmundo.uecdn.es/rss/internacional.xml'
        elif eleccion =='7':
            print('Has elegido la seccion España')
            url=self.url='https://e00-elmundo.uecdn.es/rss/espana.xml'
        return url

    def menu_elPais(self,nombre):
        menu=f"""{nombre}Has elegido el Pais, escoge la seccion que deseas comparar:
        1-Portada
        2-España
        3-Economia
        4-Deportes
        5-Sociedad
        6-Educacion
        7-Medio Ambiente
        8-Ciencia
        9-Salud
        10-Tecnologia
        11-Cultura
        12-Television
        13-Gente
        14-Internacional
        """
        seccion=input(menu)
        url=""
        if seccion=='1':
            print('Has elegido la portada')
            url=self.url='https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada'
        elif seccion =='2':
            print('Has elegido la seccion: España')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/espana'
        elif seccion =='3':
            print('Has elegido la seccion: Economia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/economia'
        elif seccion =='4':
            print('Has elegido la seccion: Deportes')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/deportes'
        elif seccion =='5':
            print('Has elegido la seccion: Sociedad')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/sociedad'
        elif seccion =='6':
            print('Has elegido la seccion: Educacion')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/educacion'
        elif seccion =='7':
            print('Has elegido la seccion: Medio Ambiente')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/clima-y-medio-ambiente'
        elif seccion =='8':
            print('Has elegido la seccion: Ciencia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/ciencia'
        elif seccion =='9':
            print('Has elegido la seccion: Salud')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/salud-y-bienestar'
        elif seccion =='10':
            print('Has elegido la seccion: Tecnologia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/tecnologia'
        elif seccion =='11':
            print('Has elegido la seccion: Cultura')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/cultura'
        elif seccion =='12':
            print('Has elegido la seccion: Television')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/television'
        elif seccion =='13':
            print('Has elegido la seccion: Gente')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/gente'
        elif seccion =='14':
            print('Has elegido la seccion: Internacional')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/internacional'
        
        return url
    
    def menu_elDiario(self,nombre):
        menu=f"""Elige una de las siguientes secciones dle periodico:
        1-Portada
        2-Internacional
        3-Economia
        4-Cultura
        5-Educacion
        6-Clima
        7-Desalambre
        8-Igualdad
        9-Politica"""

        seccion=input(menu)
        url=""
        if seccion=='1':
            print('Has elegido la portada')
            url=self.url='https://www.eldiario.es/rss/'
        elif seccion =='2':
            print('Has elegido la seccion: España')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/espana'
        elif seccion =='3':
            print('Has elegido la seccion: Economia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/economia'
        elif seccion =='4':
            print('Has elegido la seccion: Deportes')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/deportes'
        elif seccion =='5':
            print('Has elegido la seccion: Sociedad')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/sociedad'
        elif seccion =='6':
            print('Has elegido la seccion: Educacion')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/educacion'
        elif seccion =='7':
            print('Has elegido la seccion: Medio Ambiente')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/clima-y-medio-ambiente'
        elif seccion =='8':
            print('Has elegido la seccion: Ciencia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/ciencia'
        elif seccion =='9':
            print('Has elegido la seccion: Salud')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/salud-y-bienestar'
        elif seccion =='10':
            print('Has elegido la seccion: Tecnologia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/tecnologia'
        elif seccion =='11':
            print('Has elegido la seccion: Cultura')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/cultura'
        elif seccion =='12':
            print('Has elegido la seccion: Television')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/television'
        elif seccion =='13':
            print('Has elegido la seccion: Gente')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/gente'
        elif seccion =='14':
            print('Has elegido la seccion: Internacional')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/internacional'
        
        return url




washingtonPost=WashingtonPost()
elMundo=ElMundo()
#menus=Menus()
#seccion =Seccion()
#seccion_wp=Seccion_wp()
#washingtonPost=WashingtonPost()
