# utilisation de os.path.join() pour construire le chemin du fichier de manière portable
import os
import shutil
import datetime
# construction du chemin du fichier de manière portable
file_path = os.path.join('mission_data', 'missions.json')

print(f"Le chemin du fichier est: {file_path}")

# copie du fichier journal_bord.txt dans le dossier de mission_data/archives en utilisnt shutil.copy()
date_jour = datetime.datetime.now().date()
source_file = os.path.join('mission_data', 'journal_bord.txt')
destination = os.path.join('mission_data', 'archives', 'journal_bord__' + str(date_jour) + '.txt')

shutil.copy(source_file, destination)

chemin = os.getcwd()
espace = shutil.disk_usage(chemin)
print(espace.free)

# Filter les resultats de os.environ pour afficher uniquement les variables d'environnement liées à PYTHON ou PATH
python_env_vars = {key: value for key, value in os.environ.items() if 'PYTHON' in key or 'PATH' in key}

# enregistrement des differentes informations dans le fichier mission_data/rapports/rapport_systeme.txt

with open('mission_data/rapports/rapport_systeme.txt', 'w') as file:
    file.write(f"Chemin du repertoire de travail actuel: {chemin}\n")
    file.write(f"Espace libre sur le disque: {espace.free} bytes\n")
    file.write("Variables d'environnement liées à PYTHON ou PATH:\n")
    for key, value in python_env_vars.items():
        file.write(f"{key}: {value}\n")
    
# RESUMER DES OPERATIONS REALISEES
print(":::::::::: OPERATIONS REALISEES ::::::::::")
print(f"1. Le chemin du fichier missions.json a été construit de manière portable: {file_path} \n 2. Le fichier journal_bord.txt a été copié dans le dossier mission_data/archives avec un nom incluant la date du jour: {destination} \n 3. L'espace libre sur le disque a été affiché: {espace.free} bytes \n 4. Les variables d'environnement liées à PYTHON ou PATH ont été filtrées et enregistrées dans le fichier rapport_systeme.txt")
