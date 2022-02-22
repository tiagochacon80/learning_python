#Écrivez un programme qui lit deux nombres entiers et les compare. affichage d'un message à l'écran :
#- La première valeur est plus élevée
#- La deuxième valeur est plus élevée
#- Il n'y a pas de plus grande valeur, les deux sont égaux
premier = int(input("Premier nombre: "))
deuxieme = int(input("Deuxième nombre: "))
if premier > deuxieme:
    print("Le premier est plus grand")
elif premier < deuxieme:
    print("Le deuxième est plus grand")
else:
    print("Les deux nombres sont égaux")