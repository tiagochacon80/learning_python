nom = input("Entrez le nom au complet: ").strip()# Cette function élimine les espace vide avant et après
print("Analyse en cours...")
print("Toute majuscules {}".format(nom.upper()))
print("Toute minuscule {}".format(nom.lower()))
print("Le nom au complet a {} lettres".format(len(nom)-nom.count(' '))) #Ici il va eliminer le espace vide entre les noms
separer = nom.split() #Variable pour séparer les noms
print("Le prenom est {} et il a {} lettres".format(separer[0], len(separer[0]))) #Il imprime le prenom dans la position 0 et il compte les lettres