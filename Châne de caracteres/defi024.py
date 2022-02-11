#Faire un programme qui lit un nom d'une ville et dit s'elle commence par le nom "saint" ou non
ville = str(input("Entrez le nom de la ville: ")).strip()
print(ville[:5].upper() == 'SAINT') #Vérifier si dans les position 0 au 4 a le nom saint, même un majiscule ou miniscule

#Dans ce défi j'ai appris à trouver un certain string dans une phrase, même si l'utilisateur a mis des espaces inutiles ou ce string est majuscule ou minuscule.

