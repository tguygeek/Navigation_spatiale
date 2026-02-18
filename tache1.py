# Recuperation des information du ficher journal

with open("mission_data/journal_bord.txt", "r") as file:
    journal = file.readlines()
    file.close()

#Nombre de ligne du fichier journal
print(len(journal))
# Ligne du journal de contenant le mot alerte    
for line in journal:
    if "alerte" in line.lower():
        print(line)

# Enregistrement des alertes dans le fichier alerte.txt

with open("mission_data/alertes.txt", "w") as file:
    for line in journal:
        if "alerte" in line.lower():
            file.write(line)

    