## Comment ça marche ?
Téléchargement direct
Choix du mode : Le script commence par demander à l'utilisateur s'il souhaite télécharger une vidéo par son titre (y) ou directement via un lien (n).
Entrée de l'utilisateur : Selon le choix, l'utilisateur est invité à entrer soit le titre de la vidéo soit son lien YouTube direct.
Par titre : Si le titre est choisi, le script utilise youtubesearchpython pour rechercher le titre sur YouTube et affiche les 5 premiers résultats. L'utilisateur peut alors choisir quelle vidéo télécharger en entrant le numéro correspondant.
Par lien : Si un lien direct est fourni, le script passe directement à l'étape de téléchargement.
Téléchargement : Avant de télécharger, l'utilisateur est interrogé sur le fait de vouloir seulement l'audio (y) ou la vidéo complète. Le script sélectionne ensuite le flux approprié et lance le téléchargement dans le dossier courant.
Détails techniques
Gestion des erreurs : Si le lien fourni n'est pas valide, le script affiche un message d'erreur et s'arrête.
Téléchargement : Utilise pytube pour récupérer les informations de la vidéo et télécharger le fichier désiré. En mode audio, le script choisit le meilleur flux audio disponible. En mode vidéo, il sélectionne la résolution la plus élevée.
Contribution
Votre participation est encouragée ! Pour proposer des améliorations ou de nouvelles fonctionnalités, veuillez ouvrir une issue ou soumettre une pull request.

## Prérequis

Avant de commencer, assurez-vous de répondre aux exigences suivantes :

- Vous avez installé Python 3.x sur votre ordinateur.
- Vous avez installé les packages Python requis`.

## Installation
Pour installer les packages Python nécessaires, exécutez les commandes suivante :
- pip install pytube youtubesearchpython

## Auteur
- Nom : Justin Chaput
- Contact : justinchaps@hotmail.com

## Licence
Distribué sous la Licence General Public License(GNU). Voir le fichier LICENSE pour plus d'informations.
