#Faites un programme qui lit n'importe quelle année et indique s'il s'agit d'une année bissextile.
#Version 1
annee = int(input("Entrez un année: "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("La année de {} est bissextile".format(annee))
else:
    print("L'année {} n'est pas bissextile".format(annee))

#version 2

