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

# Exécution de la requête SQL pour calculer la capacité totale
requete_sql = "SELECT SUM(capacite) AS capacite_totale FROM salle"
curseur.execute(requete_sql)

# Récupération du résultat
resultat = curseur.fetchone()
capacite_totale = resultat[0]

# Affichage du résultat
print(f"La capacité totale des salles est de {capacite_totale} personnes")

# Fermeture du curseur et de la connexion
curseur.close()
connexion.close()
