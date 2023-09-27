import requests
from bs4 import BeautifulSoup
import time
import ssl
import feedparser
from newspaper import Article


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
        #para evitar problemas de certificados(sol temportal)
        ssl._create_default_https_context = ssl._create_unverified_context
        feed=feedparser.parse(url)
        #print(feed)
        #extrayendo enlaces portada em
        urls=[]
        if 'entries' in feed:
            for entry in feed.entries:
                url=entry.link
                urls.append(url)
        """
        for url in urls:
            noticia=Article(url)
            noticia.download(url)
            texto=noticia.text
        print(f'El texto de la noticia es: {texto}')
        
        #print (urls)

        return urls,texto
        """
            

        return urls

            
    
washingtonPost=WashingtonPost()
elMundo=ElMundo()

"""
urls_wp=washingtonPost.extraccion_wp()
#washingtonPost.portada_wp(urls_wp)
menu_washingtonPost.menu_wp(urls_wp)"""