nome = input("Entrez le nom au complet: ").strip()# Cette function élimine les espace vide avant et après
print("Analyse en cours...")
print("Toute majuscules {}".format(nome.upper()))
print("Toute minuscule {}".format(nome.lower()))
print("Le nom au complet a {} lettres".format(len(nome)-nome.count(' '))) #Ici il va eliminer le espace vide entre les noms
separer = nome.split() #Variable pour séparer les noms
print("Le prenom est {} et il a {} lettres".format(separer[0], len(separer[0]))) #Il imprime le prenom dans la position 0 et il compte les lettres