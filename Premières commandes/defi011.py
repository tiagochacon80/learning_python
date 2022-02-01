#Faire un programme qui calcule la superficie d'un mur sachant que la quantité de peinture se mesure en mètres carrés
#sachant que chaque litre de peinture peint une surface de 2 mètres carrés

largeur = int(input("Informez la largeur du murs: "))
hauteur = int(input("Informez l'hauteur du murs: "))
mettre_carre = float(largeur * hauteur)
galon = mettre_carre / 2
print('La surfase est de {} mettres carrés'.format(mettre_carre))
print('La quantite de litres de galon que vous avez besoin est {}l'.format(galon))