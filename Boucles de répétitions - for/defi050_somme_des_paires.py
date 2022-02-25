#Développez un programme qui lit six nombres entiers et affiche la somme de ceux qui sont pairs uniquement. Si la valeur saisie est impaire, ignorez-la.
somme = 0
accumulateur = 0
for conteur in range(0, 6):
    nombre = int(input("Entrez um nombre: "))
    if nombre % 2 == 0:
        somme += nombre
        accumulateur += 1
print(somme)
print(f"{accumulateur} nombre(s) paires et la somme est {somme}")