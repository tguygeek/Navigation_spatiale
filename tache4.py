# fonction charge_json_securise

import json


def charger_json_securise(nom_fichier):
    try:
        with open(nom_fichier, "r") as file:
            data = json.load(file)
            file.close()
        print(f"Le fichier {nom_fichier} a été chargé avec succès.")
        return data
    except FileNotFoundError:
        print(f"Erreur: le fichier {nom_fichier} n'existe pas.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur: le fichier {nom_fichier} n'est pas un fichier JSON valide.")
        return None
    
# Test de la fonction charge_json_securise

# Cas 1 : fichier normal
data = charger_json_securise("mission_data/missions.json")

# Cas 2 : fichier inexistant
data = charger_json_securise("mission_data/fantome.json")

# Cas 3 : créez un fichier corrompu pour tester
with open("mission_data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")
data = charger_json_securise("mission_data/corrompu.json")

