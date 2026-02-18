# verification de l'existantance du repertoire mission_data
import os

if os.path.exists("mission_data"):
    print("Le repertoire mission_data existe")
else:
    print(":::::::ERREUR LE REPERTOIRE MISSION_DATA N'EXISTE PAS :::::::")

# Affichage du contenu du repertoire mission_data
print("Contenu du repertoire mission_data :")
for item in os.listdir("mission_data"):
    print(item)