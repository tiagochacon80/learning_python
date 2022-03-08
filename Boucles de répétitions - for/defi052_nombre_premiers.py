#Écrivez un programme qui lit un nombre entier et indique s'il s'agit d'un nombre premier ou non.
numero = int(input("Entrez un numéro entier: "))
conteur = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f"\033[33m", end='')
        conteur += 1
    else:
        print(f"\033[32m", end='')
    print(f"{c}", end=' ')
print(f"Le numero a ete divise {conteur}")

if conteur == 2:
    print("Le numero est premier")
else:
    print("Le nombre n'est pas premier")



