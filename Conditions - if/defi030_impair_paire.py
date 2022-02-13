#Créer un programme qui lit un nombre et dit s'il est paire ou impaire

nombre = int(input("Entrez un nombre entier: "))
if nombre % 2 == 0:
    print("Ce nombre est paire")
else:
    print("Ce nombre est impaire")