import nltk
from newspaper import Article


#para almacenar el script principal
def coger_noticias(url):
    #pasando a la variable el objeto articulo con la url corr
    noticia=Article(url)

    #setups para aplicar npl
    noticia.download()
    noticia.parse()

    #tokenizacion de textos amplios, divide el texto en frases individuales
    noticia.download("punkt")
    #llamando funcion  nlp una vez simplificado el texto
    noticia.nlp()

    #accediendo a la instancia autor dentro de la clase noticia
    print('Autor:' + str(noticia.authors) + '\n')

    fecha=noticia.publish_date
    print('Fecha de publicacion: ' +str(fecha.strftime("%m/%d/%Y") + '\n'))

    #hacer resumen noticia
    print(f'Resumen de la noticia:\n\t {noticia.summary} \n')
    print('Imagen principal:\n ' +str(noticia.top_image))
    imagenes='Todas las imagenes:'
    for imagen in noticia.images:
        imagenes+='\n\t'+ imagen
    print(imagenes)
    return noticia.summary

    


#coger_noticias('https://www.nytimes.com/live/2023/08/30/us/hurricane-idalia-florida')

