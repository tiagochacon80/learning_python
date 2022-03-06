def conteur(* num): #Le * avant "num" indique qu'il va recevoir des paramètres, mais on ne sais pas combien
    for valeur in num:
        print(valeur, end=' ')
    print('FIN')

conteur(2, 1, 7)
conteur(8, 0)
conteur(4, 4, 7, 6, 2)

def conteur(* num):
    taille = len(num)
    print(f"Le total de nombres est {taille}")

conteur(2, 1, 7)
conteur(8, 0)
conteur(4, 4, 7, 6, 2)

