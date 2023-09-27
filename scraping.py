import nltk
from newspaper import Article

#url='https://www.washingtonpost.com/'
#para almacenar el script principal
def coger_noticias(url):
    #pasando a la variable el objeto articulo con la url corr
    noticia=Article(url)
    #noticia=newspaper.Article(url)

    #setups para aplicar npl
    noticia.download()
    noticia.parse()
    print('----------')

    #tokenizacion de textos amplios, divide el texto en frases individuales
    noticia.download("punkt")
    #llamando funcion  nlp una vez simplificado el texto
    noticia.nlp()

    print(f'Titulo de la noticia: {noticia.title}')

    #accediendo a la instancia autor dentro de la clase noticia
    print('Autor:' + str(noticia.authors) + '\n')

    fecha=noticia.publish_date
    print('Fecha de publicacion: ' +str(fecha.strftime("%m/%d/%Y") + '\n'))

    #hacer resumen noticia
    print(f'Resumen de la noticia:\n\t {noticia.summary} \n')
    print(f'Texto completo de la noticia:\n {noticia.text}')
    print('Imagen principal:\n ' +str(noticia.top_image))
    imagenes='Todas las imagenes:'
    for imagen in noticia.images:
        imagenes+='\n\t'+ imagen
    #print(imagenes)
    return noticia.text


def scraping_elDiario(urls):
    for url in urls:
        if 'published_parsed' in url:
            fecha_publicacion = url.published_parsed
            # Convertir la fecha en un formato legible
            fecha_formateada = f"{fecha_publicacion.tm_mday}/{fecha_publicacion.tm_mon}/{fecha_publicacion.tm_year}"
            # Imprimir la fecha de publicación
            print(f"Fecha de publicación: {fecha_formateada}")
        return fecha_formateada

    


#coger_noticias('https://www.nytimes.com/live/2023/08/30/us/hurricane-idalia-florida')

