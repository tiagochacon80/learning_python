#Développez un programme qui lit six nombres entiers et affiche la somme de ceux qui sont pairs uniquement. Si la valeur saisie est impaire, ignorez-la.
somme = 0
conteur = 0
for c in range(1, 7):
    num = int(input(f"Entrez le {c}º nombre: "))
    if num % 2 == 0:
        somme += num
        conteur += 1
print(f"Vouz avez informé {conteur} nombres et la somme est {somme}")

