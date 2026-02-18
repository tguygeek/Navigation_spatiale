# chargement du fichier mission.json
import json

with open('mission.json', 'r') as file:
    data = json.load(file)
    file.close()

# affichage de la liste des missions

for mission in data['missions']:
    print(f"[{mission['id']}] {mission['nom']} -> {mission['destination']} | {mission['duree_jours']} jours | Equipage: {mission['equipage']} | Budget: {mission['budget_millions_usd']} M$")

# Calcule et affichage du budget total de toutes les missions
budget_total = 0
for mission in data['missions']:
    budget_total += mission['budget_millions_usd']

print(f"\nBudget total de toutes les missions: {budget_total} M$")

# determination de la mission la plus longue et de la mission la plus courte
min_duree =  data['missions'][0]['duree_jours']
max_duree =  data['missions'][0]['duree_jours']

for mission in data['missions']:
    if mission['duree_jours'] < min_duree:
        min_duree = mission['duree_jours']
        mission_courte = mission['nom']
    if mission['duree_jours'] > max_duree:
        max_duree = mission['duree_jours']
        mission_longue = mission['nom']

print(f"\nLa mission la plus courte est: {mission_courte} avec une durée de {min_duree} jours.")
print(f"La mission la plus longue est: {mission_longue} avec une durée de {max_duree} jours.")


