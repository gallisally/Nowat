import time
from extracciones.extraccion_nyt import *
from procesamiento import extraer_nyt,scraping_sentimientos,procesar_guardar_periodico
from extracciones.extraccion_varias import WashingtonPost,ElMundo
from bbdd.create_db import *

import sys
import os


class Menus:
    def __init__(self):
        self.nombre=""

    def ocultar(self):
        self.salida_original = sys.stdout  # Guarda la salida estándar original
        sys.stdout = open(os.devnull, 'w')  # Redirige la salida a /dev/null

    def mostrar(self):
        sys.stdout.close()  # Cierra el archivo de salida
        sys.stdout = self.salida_original 

    def procesar_todos_los_periodicos(self):
        conn,cursor=conexion_bbdd()
        seccion = Seccion()
        
        # Diccionario que contiene información sobre los periódicos y sus secciones
        periodicos = {
         
            'La Vanguardia':[
                ('Portada','https://www.lavanguardia.com/rss/home.xml'),
                ('Internacional','https://www.lavanguardia.com/rss/internacional.xml'),
                ('Politica','https://www.lavanguardia.com/rss/politica.xml'),
                ('Vida','https://www.lavanguardia.com/rss/vida.xml'),
                ('Deportes','https://www.lavanguardia.com/rss/deportes.xml'),
                ('Economia','https://www.lavanguardia.com/rss/economia.xml'),
                ('Opinion','https://www.lavanguardia.com/rss/opinion.xml'),
                ('Cultura','https://www.lavanguardia.com/rss/cultura.xml'),
                ('Gente','https://www.lavanguardia.com/rss/gente.xml'),
                ('Sucesos','https://www.lavanguardia.com/rss/sucesos.xml'),
                ('Participacion','https://www.lavanguardia.com/rss/participacion.xml')

            ],

            'abc':[
                
                ('Portada','https://www.abc.es/rss/atom/portada/'),
                #('Portada','https://www.abc.es/rss/2.0/portada/'),
                ('Ultima hora','https://www.abc.es/rss/2.0/ultima-hora/'),
                ('Opinion','https://www.abc.es/rss/2.0/opinion/'),
                ('España','https://www.abc.es/rss/2.0/espana/'),
                ('Economia','https://www.abc.es/rss/2.0/economia/'),
                ('Internacional','https://www.abc.es/rss/2.0/internacional/'),
                ('Deportes','https://www.abc.es/rss/2.0/deportes/'),
                ('Sociedad','https://www.abc.es/rss/2.0/sociedad/'),
                ('Cultura','https://www.abc.es/rss/2.0/cultura/'),
                ('Gente','https://www.abc.es/rss/2.0/gente/'),
                ('Esitlo','https://www.abc.es/rss/2.0/estilo/'),
                ('Play','https://www.abc.es/rss/2.0/play/')

            ],

            'La Razon':[
                ('Portada','https://www.larazon.es/'),
                ('España','https://www.larazon.es/espana/'),
                ('Internacional','https://www.larazon.es/internacional/'),
                ('Economia','https://www.larazon.es/economia/'),
                ('Sociedad','https://www.larazon.es/sociedad/'),
                ('Opinion','https://www.larazon.es/opinion/'),
                ('Salud','https://www.larazon.es/salud/'),
                ('Deportes','https://www.larazon.es/deportes/'),
                ('Cultura','https://www.larazon.es/cultura/'),
                ('Gente','https://www.larazon.es/gente/'),
                ('25 aniversario','https://www.larazon.es/25-aniversario/'),
                ('Motor','https://www.larazon.es/motor/')
            ],
            'elDiario.es':[
                
                ('Portada-rss','https://www.eldiario.es/rss/'),
                ('Internacional','https://www.eldiario.es/rss/internacional/'),
                ('Economia','https://www.eldiario.es/rss/economia/'),
                ('Cultura','https://www.eldiario.es/rss/opinion/'),
                ('Educacion','https://www.eldiario.es/rss/focos/educacion/'),
                ('Clima y Medio Ambiente','https://www.eldiario.es/rss/focos/crisis-climatica/'),
                ('Desalambre','https://www.eldiario.es/rss/desalambre/'),
                ('Igualdad','https://www.eldiario.es/rss/focos/igualdad/'),
                ('Politica','https://www.eldiario.es/rss/politica/')
            ],
            
            'El Confidencial':[
               
                #('Opinion','https://rss.blogs.elconfidencial.com/'),
                ('Portada RSS','https://www.elconfidencial.com/rss/'),
                ('Portada','https://www.elconfidencial.com/'),
                ('España','https://www.elconfidencial.com/espana/'),
                ('Economia','https://www.elconfidencial.com/mercados/'),
                ('Opinion','https://blogs.elconfidencial.com/'),
                ('Salud','https://www.alimente.elconfidencial.com/'),
                ('Internacional','https://www.elconfidencial.com/mundo/'),
                ('Cultura','https://www.elconfidencial.com/cultura/'),
                ('Tecnologia','https://www.elconfidencial.com/tecnologia/'),
                ('Deportes','https://www.elconfidencial.com/deportes/'),
                ('Alma,Corazon y Vida','https://www.elconfidencial.com/alma-corazon-vida/'),
                ('Television','https://www.elconfidencial.com/television/'),
                
                ('Actualidad (mundo)','https://rss.elconfidencial.com/mundo/'),
                ('Actualidad(España)','https://rss.elconfidencial.com/espana/'),
                ('Actualidad(Comunicacion)','https://rss.elconfidencial.com/comunicacion/'),
                ('Actualidad(Sociedad)','https://rss.elconfidencial.com/sociedad/'),
                ('Opinion','https://rss.blogs.elconfidencial.com/'),
                ('Economia','https://rss.elconfidencial.com/mercados/'),
                ('Tecnologia','https://rss.elconfidencial.com/tecnologia/'),
                ('Deportes','https://rss.elconfidencial.com/deportes/'),
                ('Alma,corazon y vida','https://rss.elconfidencial.com/alma-corazon-vida/'),
                ('Cultura','https://rss.elconfidencial.com/cultura/'),
                ('Alimente','https://rss.alimente.elconfidencial.com/')


            ],
            'Al-Masdar':[
                ('Portada','https://al-masdaronline.net/'),
                ('Nacional','https://al-masdaronline.net/section/national'),
                ('local','https://al-masdaronline.net/section/local'),
                ('Derechos humanos','https://al-masdaronline.net/section/humanrights')
            ],
             '404':[
                ('Portada','https://cuatrocerocuatro.org/feed/')
            ],
            
           
            'New York Times': [
                ('Portada del dia', 'https://www.nytimes.com/'),
                ('Politica', 'https://www.nytimes.com/section/politics'),
                ('Salud', 'https://www.nytimes.com/section/health'),
                ('Negocios', 'https://www.nytimes.com/section/business'),
                ('Opinion', 'https://www.nytimes.com/section/opinion'),
                ('Tecnologia', 'https://www.nytimes.com/section/technology')
           ],
    
               
             'El Mundo': [
                ('Portada','https://e00-elmundo.uecdn.es/rss/portada.xml'),
                ('Opinion','https://e00-elmundo.uecdn.es/rss/opinion.xml'),
                ('Economia','https://e00-elmundo.uecdn.es/rss/economia.xml'),
                ('Deportes','https://e00-elmundo.uecdn.es/rss/deportes.xml'),
                ('Ciencia y Salud','https://e00-elmundo.uecdn.es/rss/ciencia-y-salud.xml'),
                ('Internacional','https://e00-elmundo.uecdn.es/rss/internacional.xml'),
                ('España','https://e00-elmundo.uecdn.es/rss/espana.xml')
            ],
            
            'El Pais':[
                ('Portada','https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada'),
                ('España','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/espana'),
                ('Economia','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/economia'),
                ('Deportes','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/deportes'),
                ('Sociedad','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/sociedad'),
                ('Educacion','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/educacion'),
                ('Medio Ambiente','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/clima-y-medio-ambiente'),
                ('Ciencia','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/ciencia'),
                ('Salud','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/salud-y-bienestar'),
                ('Tecnologia','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/tecnologia'),
                ('Cultura','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/cultura'),
                ('Television','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/television'),
                ('Gente','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/gente'),
                ('Internacional','https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/internacional')
            ] 
    
        }
             
            # Repetir el mismo patrón para los demás periódicos
        

        # Iteramos sobre el diccionario de periódicos
        for periodico, secciones in periodicos.items():
            #subjetividad_periodico = []
            print(f'Procesando {periodico}')
            #self.ocultar()
            
            if periodico =='New York Times':
                print('Procesando NYT')  
                nombre_medio='New York Times'
                tipo_medio='periodico'          
                #procesar_guardar_periodico(secciones,conn,cursor,nombre_medio,tipo_medio)       
            elif periodico=='El Mundo':
                #elMundo=ElMundo()
                print('Procesando el Mundo')
                nombre_medio='El Mundo'
                tipo_medio='periodico'
            elif periodico=='El Pais':
                nombre_medio='El Pais'
                tipo_medio='periodico'
            elif periodico=='elDiario.es':
                nombre_medio='elDiario.es'
                tipo_medio='periodico'
            elif periodico =='404':
                nombre_medio='404'
                tipo_medio='periodico'
            elif periodico=='Al-Masdar':
                nombre_medio='Al-Masdar'
                tipo_medio='periodico'
            elif periodico=='El Confidencial':
                nombre_medio='El Confidencial'
                tipo_medio='periodico'
            elif periodico=='La Razon':
                nombre_medio= 'La Razon'
                tipo_medio='periodico'
            elif periodico=='abc':
                nombre_medio='ABC'
                tipo_medio='periodico'
            elif periodico=='La Vanguardia':
                nombre_medio='La Vanguardia'
                tipo_medio='periodico'
            elif periodico=='20minutos':
                nombre_medio='20minutos'
                tipo_medio='periodico'
            elif periodico =='cnn':
                nombre_medio='cnn'
                tipo_medio='periodico'
            

            
            procesar_guardar_periodico(secciones,conn,cursor,nombre_medio,tipo_medio) 


          

        print('Procesamiento completado')
        

    
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
                url,seccion=seccion.nyt_menu(self.nombre)
                urls=extraer_nyt(url)
                url=scraping_sentimientos(urls)
                
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
                procesar_elMundo(url)
                
            
            elif eleccion=='4':
                print('Abriendo El Pais')
                url=seccion.menu_elPais(self.nombre)
                procesado=procesar_elMundo(url)
                
            elif eleccion =='5':
                print('Abriendo elDiario.es')
                url=seccion.menu_elDiario(self.nombre)
                procesado=procesar_elDiario(url)
                
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
                seccion='portada'
                 
                
            elif eleccion=='2':
                print('Abriendo seccion politica del NYT')
                url=self.url=('https://www.nytimes.com/section/politics')
                seccion='politica'
                
            elif eleccion=='3':
                print('Abriendo seccion Salud del NYT')
                url=self.url='https://www.nytimes.com/section/health'
                seccion='salud'
            elif eleccion=='4':
                print('Abriendo seccion de Negocios del NYT')
                url=self.url='https://www.nytimes.com/section/business'
                seccion='negocios'
            elif eleccion =='5':
                print('Abriendo seccion Opinion del NYT')
                url=self.url='https://www.nytimes.com/section/opinion'
                seccion='opinion'
            elif eleccion=='6':
                print('Abriendo seccion de Tecnologia del NYT')
                url=self.url='https://www.nytimes.com/section/technology'
                seccion='tecnologia'
            else:
                print('Esta opcion aun no esta programada. Por favor, mete la opcion correcta')   
            return url,seccion
        
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
        6-Clima y Medio Ambiente
        7-Desalambre
        8-Igualdad
        9-Politica"""

        seccion=input(menu)
        url=""
        if seccion=='1':
            print('Has elegido la portada')
            url=self.url='https://www.eldiario.es/rss/'
        elif seccion =='2':
            print('Has elegido la seccion: Internacional')
            url=self.url='https://www.eldiario.es/rss/internacional/'
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
            print('Has elegido la seccion: Clima y Medio Ambiente')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/clima-y-medio-ambiente'
        elif seccion =='8':
            print('Has elegido la seccion: Ciencia')
            url=self.url='https://feeds.elpais.com/mrss-s/list/ep/site/elpais.com/section/ciencia'
        elif seccion =='9':
            print('Has elegido la seccion: Politica')
            url=self.url='https://www.eldiario.es/rss/politica/'
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
seccion =Seccion()
#seccion_wp=Seccion_wp()
#washingtonPost=WashingtonPost()
