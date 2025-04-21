# main.py

from scraper import scrape_avis  # Fonction pour extraire les avis
from db_utils import init_db, insert_avis  # Fonctions pour gérer la base

def main():
    print("📡 Lancement du scraping...")
    avis = scrape_avis()  # Récupère les avis depuis le site

    print(f"✅ {len(avis)} avis récupérés.")

    print("💾 Initialisation de la base de données...")
    init_db()  # Crée la base et la table si besoin

    print("📥 Insertion des avis dans la base...")
    insert_avis(avis)  # Insère tous les avis dans la base

    print("🎉 Fin du processus.")

# Lance le script seulement s’il est exécuté directement
if __name__ == "__main__":
    main()
