#Faire un programme que lit un numéro et affiche sa table de multiplication.
numero = int(input("Entrez un numéro: "))
resultat = 0
multiplicateur = 0
while multiplicateur <= 9:
    resultat = numero * multiplicateur
    print(numero, 'x', multiplicateur, '=', resultat)
    multiplicateur = multiplicateur + 1

