# scraper.py

import requests  # Pour envoyer des requêtes HTTP vers le site web
from bs4 import BeautifulSoup  # Pour analyser le contenu HTML
from config import URL, HEADERS  # On importe l'URL et les headers définis dans config.py

def scrape_avis():
    # Envoie une requête GET à l'URL cible avec les headers
    response = requests.get(URL, headers=HEADERS)

    # Parse le contenu HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Récupère toutes les balises <p> contenant les avis (classe CSS utilisée par Trustpilot)
    avis_html = soup.find_all("p", attrs={"data-relevant-review-text-typography": "true"})


    # Nettoie chaque avis (on supprime les espaces inutiles) et crée une liste
    avis_list = [a.text.strip() for a in avis_html]

    return avis_list  # Renvoie la liste d’avis extraits
