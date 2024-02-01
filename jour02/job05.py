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

# Exécution de la requête SQL pour calculer la superficie totale
requete_sql = "SELECT SUM(superficie) AS superficie_totale FROM etage"
curseur.execute(requete_sql)

# Récupération du résultat
resultat = curseur.fetchone()
superficie_totale = resultat[0]

# Affichage du résultat
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermeture du curseur et de la connexion
curseur.close()
connexion.close()
