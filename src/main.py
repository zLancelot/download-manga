import requests
import shutil
import json

def print_info_mangas(mangas):
    for manga in mangas:
        print ("\n")
        print (f'ID: {manga["id"]}')
        print (f'Name: {manga["name"]}')

with open('data/mangas.json', 'r') as f:
    mangas = json.load(f)

while (1):
    try:
        print_info_mangas(mangas)

        manga_id = int(input("\nChoose an ID: "))
        
        manga = mangas[manga_id-1]
        
        break
    except ValueError:
        print ("_"*50)
        print ("\n\n  # Invalid Value #")
    except IndexError:
        print ("_"*50)
        print ("\n\n  # Choose an ID below #")


print (manga)

url = f'http://mangas2019.centraldemangas.com.br/{manga["name_url"]}/{manga["name_url"]}196-01.jpg'

headers = {
    "Referer": f'http://centraldemangas.online/titulos/{manga["name_referer_header"]}/manga/ler-online/196'
}

response = requests.get(url, stream=True, headers=headers)

with open('img1.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response