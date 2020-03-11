import requests
import shutil
import json

def print_info_mangas(mangas):
    for manga in mangas:
        print ("\n")
        print (f'ID: {manga["id"]}')
        print (f'Name: {manga["name"]}')

def download_chapters_in_range(manga, initial, final):
    for c in range(initial, final+1):
        chapter = f'{"0"*(3 - len(str(c)))}{c}'
        
        file_name = f'{manga["name"]}_{chapter}.jpg'

        url = f'http://{manga["host"]}.centraldemangas.com.br/{manga["name_url"]}/{manga["name_url"]}{chapter}-01.jpg'

        headers = {
            "Referer": f'http://centraldemangas.online/titulos/{manga["name_referer_header"]}/manga/ler-online/{chapter}'
        }

        print (url)
        print (headers)
        print ("\n")

        response = requests.get(url, stream=True, headers=headers)

        with open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

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

print ("\nDigite o Intervalo de capítulos que deseja baixar. Ex: 1-5 ou 20-50")
range_chapters = input("Intervalo: ")

(chapter_initial, chapter_end) = map(int, range_chapters.split("-"))

download_chapters_in_range(manga, chapter_initial, chapter_end)