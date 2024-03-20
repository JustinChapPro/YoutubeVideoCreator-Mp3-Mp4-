from pytube import YouTube
from youtubesearchpython import VideosSearch

#Downloader permet de télécharger une vidéo par son lien
def downloader(link):
    #vérifie si le lien est valide
    try:
        video = YouTube(link)
    except:
        print("Lien invalide !")
        return

    #Demende si l'utilisateur veut télécharger uniquement l'audio
    audio_only = input("Voulez vous télécharger uniquement l'audio ? (y/n) : ")

    if audio_only == "y" or audio_only == "Y":
        stream = video.streams.filter(only_audio=True).first()
    else:
        stream = video.streams.get_highest_resolution()

    #installe la vidéo dans le dossier courant
    stream.download()

    print(f"Téléchargement terminé : {video.title}")

#Searcher permet de chercher une vidéo par son titre et va chercher le lien de la vidéo
def searcher():
    input_title = input("Entrez le titre de la vidéo : ")
    search = VideosSearch(input_title, limit=5)

    #affiche les 5 premiers résultats de la recherche
    for i, result in enumerate(search.result()["result"]):
        print(f"{i + 1}. {result['title']}")

    #demende a l'utilisateur quel vidéo il veut télécharger
    choix_video = int(input("Choisissez la vidéo que vous voulez télécharger : "))
    link = search.result()["result"][choix_video - 1]["link"]
    return link

#Demende a l'utilisateur si il veut télécharger une vidéo par son titre ou par son lien
link_title = input("Dites oui si vous voulez télécharger une vidéo par son titre : y/n ")

if link_title.lower() == "y":
    link = searcher()
else:
    link = input("Entre le lien de la vidéo a télécharger : ")

downloader(link)
