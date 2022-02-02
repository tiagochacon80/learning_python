#Prix de location d'auto

km = float(input('Informez la quantité de kilomètres roulés: '))
jours = int(input('Informez la quantité de jours loués: '))
calcule = (jours * 60) + (km * 0.15)
print("Le prix a payer pour la location d'auto est de {}".format(calcule))