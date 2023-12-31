#utilizacion para parsear webs a través de la extraccion de html
import requests
from menu import *
from bs4 import BeautifulSoup as soup
import re
from menu import *
import ssl

def extraer_nyt(url):
    ssl._create_default_https_context = ssl._create_unverified_context

    print('Extrayendo los hiperenlaces de las ultimas noticias...')
    print(url)
    nombre_medio='New York Times'
    tipo_medio='periodico'
    #time.sleep(2)
    contenido_interes=get_contenido(url)
    primeros_indices,final_indices,url=parseo_contenido(contenido_interes,url)
    urls=get_urls(primeros_indices, final_indices,contenido_interes,url)
    return urls

#para coger el string del contenido en HTML conteninedo todos los hiperliks del articulo
def get_contenido(url):

    #EXTRAYENDO TODO HTML
    pagina=requests.get(url)
    #llamando metodos de soup
    pagina_soup=soup(pagina.content, 'html.parser')
    #print(pagina_soup)

    paquete_url=pagina_soup.find_all("script", {"type" : "application/ld+json"})
    
    #inicializando lista que contendra los tags
    #EXTRAYENDO TODOS HYPERLINKS
    etiquetas=[]
    for paquete in paquete_url:
        for dictionary in paquete:
            etiquetas.append(dictionary)
    longitud=len(etiquetas)
    #print(f'Strings presentes en la lista:  {longitud}')
    print('**********************')

    #CREANDO EL STRING DEL CONTENIDO EN 1
    #quitar espacios
    etiquetas[0:2] = [''.join(etiquetas[0:2])]
    #extraccion dle primer elemento para eliminar duplicados
    contenido_interes = etiquetas[0]

    #EXTRACCION DE LA LIBRERIA Y METADATOS NECESARIOS
    #indexacion de los resultados para coger solo lo que interesa
    contenido_interes_indexado= contenido_interes.index("itemListElement")
    contenido_interes = contenido_interes[contenido_interes_indexado +18:]
    longitud_etiquetas=len(etiquetas)
    longitud_string=len(contenido_interes)
    #print(f'La lista indexada sin repeticiones contiene: {longitud_etiquetas} strings y {longitud_string} elementos')
    #print(f'el contenido de interes es: {contenido_interes}')
    print('Contenido extraido correctamente')
    return(contenido_interes)
    

  
#inicio y final de los indices de los hiperlinks de los articulos
def parseo_contenido(contenido_interes,url):
    #implementar patrones
    primeros_indices=[]
    final_indices=[]
    for i in range(len(contenido_interes)):
        #primer indice(patrones,caracter del contenido en el string)
        if contenido_interes.startswith("https://www.nytimes.com/2023",i):
            primeros_indices.append(i)  
        if contenido_interes.startswith(".html",i+5):
            final_indices.append(i)
            final_indices= [x+5 for x in final_indices]

    if len(primeros_indices)> len(final_indices):
        sobra=len(primeros_indices)- len(final_indices)
        primeros_indices=primeros_indices[:sobra]
    if len(final_indices)>len(primeros_indices):
        sobra=len(final_indices) - (len(final_indices)-len(primeros_indices))
        final_indices=final_indices[:sobra]       
    #print(primeros_indices)
    #print(final_indices)
    print('Indices extraidos correctamente')
    return primeros_indices,final_indices,url

#obteniendo los enlaces de las ultimas noticias publicadas en 2023  
def get_urls(primeros_indices, final_indices,contenido_interes,url):
    urls_sucio=[]
    urls=[]
    for i in range(len(primeros_indices)):
            urls_sucio.append(contenido_interes[primeros_indices[i]:final_indices[i]])

    #patron_url = r'https?://[^\s,"]+'
    patron_url=r'https?://[^\s,"]+\.html'

    # Filtrar las URLs válidas utilizando expresiones regulares
    urls_limpias = [re.findall(patron_url, cadena) for cadena in urls_sucio]

    # Eliminar listas vacías y aplanar la lista de URLs
    urls_limpias = [url for url in urls_limpias if url]
    urls_limpias = [url for sublist in urls_limpias for url in sublist]

# Imprimir la lista de URLs válidas
   
    print(f'Se han encontrado {len(urls_limpias)} en portada')
    print(f'Los enlaces a las noticias de este año son:\n{urls_limpias}')
    #return urls_limpias,primeros_indices,final_indices,contenido_interes,url
    return urls_limpias

    






#get_contenido('https://www.nytimes.com/section/technology')
#contenido_interes = get_contenido('https://www.elmundo.es/economia.html')
#contenido_interes = get_contenido('https://www.nytimes.com/section/technology')
#parseo_contenido(contenido_interes)
#primeros_indices,final_indices=parseo_contenido(contenido_interes)
#urls=get_urls(primeros_indices, final_indices,contenido_interes)


