# Manipuler les fichires json en ecriture

import json
from tache4 import charger_json_securise

# Creationn de la fonction ajouter mission
def ajouter_mission(chemin_json,mission):
    # Charger le fichier JSON de manière sécurisée
    donnees = charger_json_securise(chemin_json)

    #verifieer que l'id de la nouvelle mission n'existe pas déjà
    if any(m['id'] == mission['id'] for m in donnees['missions']):
        print(f"Erreur: une mission avec l'id {mission['id']} existe déjà.")
        return
    else:
        print(f"Ajout de la mission avec l'id {mission['id']}.")
        donnees['missions'].append(mission)
    # Écrire les données mises à jour dans le fichier JSON
    with open(chemin_json, 'w') as file:
        json.dump(donnees, file, indent=2)
        print(f"Le fichier {chemin_json} a été mis à jour avec succès.")
        file.close()
    
    
# Test de la fonction ajouter_mission

nouvelle = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}

ajouter_mission("mission_data/missions.json", nouvelle)

