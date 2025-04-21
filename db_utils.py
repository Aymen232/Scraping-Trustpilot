#Gestion de la base SQLite

# db_utils.py

import sqlite3  # Pour créer et manipuler une base SQLite
from datetime import datetime  # Pour ajouter un horodatage aux avis

def init_db(db_path="data/avis_trustpilot.db"):
    # Connexion à la base de données (fichier créé s'il n'existe pas)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Création de la table "avis" si elle n'existe pas déjà
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS avis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Clé primaire auto-incrémentée
            contenu TEXT,                          -- Contenu textuel de l’avis
            date_scraping TEXT                     -- Date et heure de collecte
        )
    ''')

    # Validation de la création et fermeture de la base
    conn.commit()
    conn.close()

def insert_avis(avis_list, db_path="data/avis_trustpilot.db"):
    # Connexion à la base SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insertion de chaque avis dans la base
    for contenu in avis_list:
        timestamp = datetime.now().isoformat()  # Date et heure actuelles
        cursor.execute(
            "INSERT INTO avis (contenu, date_scraping) VALUES (?, ?)",
            (contenu, timestamp)
        )

    # Validation des insertions et fermeture de la base
    conn.commit()
    conn.close()
