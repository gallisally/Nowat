import requests
from bs4 import BeautifulSoup
url='https://www.elmundo.es/'
def extraccion_em(url):
        contenido=requests.get(url)
        if contenido.status_code==200:
            html=contenido.text
            soup=BeautifulSoup(html,'html.parser')
            #print(soup)
            urls=soup.find_all('a')
            #noticias_urls = [link['href'] for link in urls if '/noticia/' in link['href']]
            
            urls=[]
            for i in urls:
                href=i.get('href')
                if href:
                    urls.append(i)
                return urls
            print('-----------')
            print(urls)
            return urls
            
            
            
        else:
            print("No se pudo acceder a la página:", contenido.status_code)    
        return urls

extraccion_em(url)

