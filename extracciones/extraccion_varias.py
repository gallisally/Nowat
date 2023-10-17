import requests
from bs4 import BeautifulSoup
from extracciones.extraccion_nyt import *
from extracciones.extraccion_varias import *
import time
import ssl
import feedparser
from newspaper import Article
from urllib.request import urlopen


def funcion_extraccion(nombre_medio, url):
    extracciones = {
        'New York Times': lambda: extraer_nyt(url),
        'El Mundo': lambda: elMundo.extraccion_em(url),
        'El Pais': lambda: elMundo.extraccion_em(url),
        'elDiario.es':lambda:elMundo.extraccion_em(url),
        '404':lambda:elMundo.extraccion_em(url),
        'Al-Masdar':lambda:elMundo.extraccion_em(url),
        'El Confidencial':lambda:elMundo.extraccion_em(url),
        'La Razon': lambda:extraccion_html(url),
        'ABC':lambda: extraccion_abc(url),
        'La Vanguardia':lambda:extraccion_abc(url),
        '20minutos':lambda:elMundo.extraccion_em(url),
        'cnn':lambda:extraccion_abc(url)
    }
    urls = extracciones.get(nombre_medio)()
    print (f'se ha extraido')
    return urls

class WashingtonPost:
    def __init__(self):
        self.url=""
    def extraccion_wp(self,url):
    # URL de la página principal de The Washington Post
        #url = "https://www.washingtonpost.com/"

        # Realizar una solicitud GET para obtener el contenido de la página
        response = requests.get(url)

        # Comprobar si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Obtener el contenido HTML de la página
            html = response.text
            # Crear un objeto BeautifulSoup para analizar el HTML
            soup = BeautifulSoup(html, "html.parser")
            # Encontrar todos los elementos "a" (enlaces) en la página
            links = soup.find_all("a")
            # Iterar a través de los enlaces e imprimir sus URLs
            lista_1=[]
            for link in links:
                href = link.get("href")
                if href:
                    lista_1.append(href)

            urls_wp=[]
            for i in lista_1:
                if i.startswith('https://www.washingtonpost.com/'):
                    urls_wp.append(i)
            #print(urls_wp)
            return urls_wp
        else:
            print("No se pudo acceder a la página:", response.status_code)    
        return urls_wp



class ElMundo:
    def __init__(self):
        self.url=""

    def extraccion_em(self,url):
        noticia=Article(url)
        noticia.download(url)
        #para evitar problemas de certificados(solucion temportal)
        ssl._create_default_https_context = ssl._create_unverified_context
        feed=feedparser.parse(url)
        urls=[]
        if 'entries' in feed:
            for entry in feed.entries:
                url=entry.link
                urls.append(url)

        for item in feed.entries:
            link=item.link
            urls.append(link)
        print (f'las urls son :{urls}')
        return urls


def extraccion_html(url):
    #realizando solicitud http para coger contenido de la url
    response=requests.get(url)
    html=response.text
    #creando objeto soup procesando html
    soup=BeautifulSoup(html,'html.parser')
    #buscando links de las noticias con etiqueta a
    enlaces=soup.find_all('a',href=True)
    urls=[]
    patron=r".*.html$"
    for a in enlaces:
        url=a['href']
        if re.match(patron,url):
            urls.append(url)
        else:
            pass
    print(urls)
    #print(f'Las urls extraidas de la razon son las siguientes:{urls}')
    return urls

def extraccion_abc(url):
    ssl._create_default_https_context = ssl._create_unverified_context

    response = urlopen(url)
    rss = response.read()
    soup=BeautifulSoup(rss,'xml')
    items=soup.find_all('item')
    urls=[]
    for item in items:
        link=item.find('link').text
        #titulo=item.find('title').text
        urls.append(link)
    print(f'las urls son_ {urls}')
    return urls



    
    
washingtonPost=WashingtonPost()
elMundo=ElMundo()

"""
urls_wp=washingtonPost.extraccion_wp()
#washingtonPost.portada_wp(urls_wp)
menu_washingtonPost.menu_wp(urls_wp)"""