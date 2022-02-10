#Faire un programme qui lit le nom au complet d'une personne et verifi s'il y a un nom Silva dans le nom.
nom = str(input("Entrez le nom au complet: ")).strip()
print("Votre nom a le nom Silva? {}".format('silva' in nom.lower()))#Il vérifie si le nom Silva est dans la variable nom, même en miniscule ou majiscule

#Dans ce défi j'ai appris à trouver un string même si l'utilisateur a mis des espaces inutiles ou ce string est majuscule ou minuscule.