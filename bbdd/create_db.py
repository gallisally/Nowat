import psycopg2
from psycopg2 import sql


def conexion_bbdd():
    claves={
        'dbname':'nowatt_db',
        'user': 'postgres',
        'password':'Nowatt55!!!',
        'host':'localhost',
        'port':'5432'
    }

    conn = psycopg2.connect(
            user=claves['user'],
            password=claves['password'],
            host=claves['host'],
            port=claves['port']
        )
    conn.autocommit = True
        
    cursor=conn.cursor()
    nombre_db='nowatt_db'
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'nowatt_db'")
    existe = cursor.fetchone()
    print(f'bbdd ya creada')
    if not existe:
    
        cursor.execute(f'CREATE DATABASE {nombre_db}')
        print(f'bd creada por primera vez')
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noticias(
                id BIGSERIAL PRIMARY KEY,
                nombre_medio VARCHAR(500),
                tipo_medio VARCHAR(50),
                url VARCHAR(10000),
                seccion VARCHAR (500),
                titulo VARCHAR(1000000),
                autor VARCHAR(500),
                fecha_publicacion DATE,
                resumen VARCHAR(1000000),
                texto TEXT,
                keywords VARCHAR(10000),
                subjetividad NUMERIC(10,5),
                polaridad NUMERIC(10,5),
                imagen_principal VARCHAR(10000),
                imagenes_2 VARCHAR(1000000)

        );
                """)
    conn.commit()
    print(f'tabla noticias creada')
    #cursor.close()
    #conn.close()
    return conn,cursor

def insercion_datos(conn,cursor,nombre_medio,tipo_medio,url,seccion,titulo_noticia,autor,fecha_publicacion,resumen,texto,keywords,media_subjetividad,media_polaridad,imagen_principal,imagenes_2):
    print('insertando noticia en la bbdd')
    print(f'la urlmetida es {url}')
    print(f'el titulo a mater es: {titulo_noticia}')
    print(f'autor metido es_{autor}')
    print(f'fecha metida :{fecha_publicacion}')
    #cursor=conn.cursor()
    #checkeando si existe url
    cursor.execute("SELECT COUNT(*) FROM noticias WHERE url= %s",(str(url),))
    contador=cursor.fetchone()[0]
    valores = (nombre_medio,tipo_medio,str(url),seccion,titulo_noticia,autor,fecha_publicacion,resumen,texto,keywords,media_subjetividad,media_polaridad,imagen_principal,imagenes_2)
    
    
    if contador == 0:
        #print(f'Datos a insertar: {nombre_medio}, {tipo_medio}, {url}, {seccion}, {titulo_noticia}, {autor}, {fecha_publicacion}, {resumen}, {texto}, {keywords}, {media_subjetividad}, {media_polaridad}, {imagen_principal}, {imagenes_2}')
        insertar_noticias="""INSERT INTO noticias(nombre_medio,tipo_medio,url,seccion,
        titulo,autor,fecha_publicacion,resumen,texto,keywords,subjetividad,polaridad,imagen_principal,imagenes_2)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING id""" 
        cursor.execute(insertar_noticias,valores)
        #en caso de querer coger el nuevo id
        #nuevo = cursor.fetchone()[0]
        conn.commit()
        print('Noticia insertada correctamente')
    else:
        print('repetido')
    #cursor.close()
    #conn.close()
    return conn,cursor