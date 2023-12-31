import nltk
from newspaper import Article
from datetime import datetime
import re
import feedparser

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
    titulo_noticia_sucio=noticia.title
    titulo_noticia=titulo_noticia_sucio.replace("'","''")
    autor_wf=noticia.authors
    autor=[autor for autor in autor_wf if not autor.startswith('More About')]
    fecha_publicacion_o=noticia.publish_date
    if fecha_publicacion_o is not None:
        fecha_publicacion=fecha_publicacion_o.strftime('%Y/%m/%d')
        fecha_publicacion_spain=fecha_publicacion_o.strftime("%m/%d/%Y")
    else:
        fecha_publicacion=None

    resumen=noticia.summary
    texto=noticia.text
    keywords_set=noticia.keywords
    keywords_list=list(keywords_set)
    keywords=','.join(keywords_list)
    imagen_principal=noticia.top_image
    imagenes_2=str(noticia.images)
    
    print(f'Titulo de la noticia: {titulo_noticia}')
    
    print(f'Autor:{autor}')

    
    if fecha_publicacion is not None:
        print('Fecha de publicacion: ' +str(fecha_publicacion_spain) + '\n')
    else:
        print('Fecha no disponible')

    #hacer resumen noticia
    #print(f'Resumen de la noticia:\n\t {resumen} \n')
    #print(f'EL texto es :\n{texto}')
    #print(f'Texto completo de la noticia:\n {texto}')
    print(f'Palabras clave de la noticia: {keywords}')
    print(f'Las etiquetas de la noticia son: {noticia.tags}')
    print('Imagen principal:\n ' +str(imagen_principal))
    imagenes='Todas las imagenes:'
    for imagen in imagenes_2:
        imagenes+='\n\t'+ imagen
    #print(imagenes)
    return titulo_noticia,autor,fecha_publicacion,resumen,texto,keywords,imagen_principal,imagenes_2



