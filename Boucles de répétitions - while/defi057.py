#Démarrez un programme qui lit le sexe d'une personne, mais n'accepte que les valeurs « M » ou « F ».
# Si c'est faux, redemandez la saisie jusqu'à ce que vous ayez une valeur correcte.

sexe = str(input("Informez votre sexe: [M/F] "))
while sexe not in "MmFf":
    sexe = str(input("Données invalides, veuillez indiquer votre sexe: "))
print("Sexe {} enregistré avec succès".format(sexe))