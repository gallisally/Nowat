from mastodon import Mastodon 
from mastodon.credenciales import CLIENT_KEY,CLIENT_SECRET,REDIRECT_URI,ACCESS_TOKEN


#creando instancia y atenticacion
mastodon = Mastodon(
    client_id= CLIENT_KEY,
    client_secret= CLIENT_SECRET,
    api_base_url= REDIRECT_URI,
    access_token=ACCESS_TOKEN
)

#autenticacion
"""mastodon.log_in(
    username='samanta_2016',
    password= 'Nowatt55tfg!',
    to_file='guardar_token.txt'
)
"""

timeline = mastodon.timeline_home()
for toot in timeline:
    print(toot['content'])

#mastodon.toot('hola marina')
hashtags_populares= mastodon.trending_tags()

for h in hashtags_populares:

    print (f"Hashtag: {h['name']}, URL:{h['url']} ")