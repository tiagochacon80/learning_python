#Faire un programme qui lit une phrase et affiche la quantite de fois qui apparaît la lettre A, affiche sa première position et la dernière.
lettre = str(input('Entrez une phrase: ')).strip().upper()
print('La phrase contient: {}'.format(lettre.count('A')))
print('Première position de A: {}'.format(lettre.find('A')))   # On commence par le 0...4,5,6
print('Dernière position de A: {}'.format(lettre.rfind('A')))  # Il commence a chercher par la droite et on commence par le 0...4,5,6

#Dans ce défi j'ai appris à compter la quantité de caractères dans une phrase, trouvé la première et dernière position d'un string.