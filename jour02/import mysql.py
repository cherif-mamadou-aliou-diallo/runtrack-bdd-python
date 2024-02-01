import mysql.connector

# Paramètres de connexion à la base de données
conn= mysql.connector.connect(
    host =  "localhost" ,    
    user = "root" ,
    password = "mySQL@231500" ,
    database = "LaPlateforme" 
)

# Connexion à la base de données

cursor = conn.cursor()

# Requête pour récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiant"

# Exécution de la requête
cursor.execute(query)

# Récupération des résultats
students = cursor.fetchall()

# # Affichage des résultats en console
# for student in students:

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
print(students)
