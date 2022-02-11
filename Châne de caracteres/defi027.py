#Faire un programme qui lit un nom au complet et affiche le premier nom et le dernier séparément.
nom_complet = str(input('Entrez le nom au complet: ')).strip()
nom = nom_complet.split() #Séparer les position des strings ['Prenom', 'nom', 'deuxième nom'...]
print("Bonjour, comment vas-tu ?")
print('Votre premier nom est: {}'.format(nom[0]))
print('Votre dernier nom est: {}'.format(nom[len(nom)-1]))#Tous les positions du string moins 1, pour trouvé le dernier

#Dans ce défi, j'ai appris à séparer les strings pour trouver sa position et indiquer quel position se trouve un certain string.

