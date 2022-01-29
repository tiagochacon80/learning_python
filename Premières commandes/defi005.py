#Faire un programme qui affiche un numéro entier, son prédécesseur et son successeur
numero = int(input("Entrez un numéro entier: "))
predecesseur = numero - 1
successeur = numero + 1
print("Le numéro est {}, son prédécesseur est {}, son successeur est {}".format(numero, predecesseur, successeur))
