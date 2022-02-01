#Faire un programme qui lit une valeur et indique combien coûte le produit avec une remise de 5%.

produit = float(input("Informez le prix du produit: "))
rabais = 0.95
prix_final = produit * rabais
print('Le prix final du produit avec rabais est de ${}'.format(prix_final))
