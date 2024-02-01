import mysql.connector

# Connexion à la base de données
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mySQL@231500",
    database="LaPlateforme"
)

# Création d'un curseur
curseur = connexion.cursor()

# Exécution de la requête SQL
requete_sql = "SELECT nom, capacite FROM salle"
curseur.execute(requete_sql)

# Récupération des résultats
resultats = curseur.fetchall()

# Affichage des résultats
for resultat in resultats:
    nom_salle, capacite_salle = resultat
    print(f"Nom de la salle: {nom_salle}, Capacité: {capacite_salle}")

# Fermeture du curseur et de la connexion
curseur.close()
connexion.close()
