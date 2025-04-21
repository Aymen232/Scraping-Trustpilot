import sqlite3  # Pour accéder à la base SQLite

# Chemin vers la base de données
db_path = "data/avis_trustpilot.db"

# Connexion à la base
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Exécution d'une requête pour récupérer les avis
cursor.execute("SELECT id, contenu, date_scraping FROM avis")

# Récupération de tous les résultats
avis = cursor.fetchall()

# Affichage propre dans le terminal
print("\n📋 Liste des avis collectés :\n")
for id_, contenu, date in avis:
    print(f"🆔 {id_} | 📅 {date}\n📝 {contenu}\n" + "-"*80)

# Fermeture propre de la base
conn.close()
