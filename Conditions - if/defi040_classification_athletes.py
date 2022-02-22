#La Confédération Nationale de Natation a besoin d'un programme qui lit l'année de naissance d'un athlète et montre sa catégorie:
#Jusqu'à 9 ans : MIRIM - Jusqu'à 14 ans : ENFANTS - Jusqu'à 19 ans : JUNIOR - Jusqu'à 25 ans : SENIOR -  Plus de 25 ans : MASTER

from datetime import date
annee_naissance = int(input("Entrez l'année de naissance: "))
annee = date.today().year
age = annee - annee_naissance
print(annee)
print("L'athlete a {} ans".format(age))
if age <= 9:
    print("Classification: MIRIM")
elif age <= 14:
    print("Classification: ENFANT")
elif age <= 19:
    print("Classification: JUNIOR")
elif age <= 25:
    print("Classification: SENIOR")
else:
    print("Classification: MASTER")