import requests
from bs4 import BeautifulSoup
import time


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
        contenido=requests.get(url)
        if contenido.status_code==200:
            html=contenido.text
            soup=BeautifulSoup(html,'html.parser')
            urls=soup.findall('a')
            urls=[]
            for i in urls:
                href=i.get('href')
                if href:
                    urls.append(i)
            print('-----------')
            return urls
        else:
            print("No se pudo acceder a la página:", contenido.status_code)    
        return urls


            
    
washingtonPost=WashingtonPost()
elMundo=ElMundo()

"""
urls_wp=washingtonPost.extraccion_wp()
#washingtonPost.portada_wp(urls_wp)
menu_washingtonPost.menu_wp(urls_wp)"""