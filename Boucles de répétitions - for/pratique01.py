n = int(input("Entrez un nombre: "))
for c in range(0, n + 1): #Le plus un (n + 1), il va arriver au nombre qui l'utilisateur a entré
    print(c)
print("FIM")

print("------------------")

i = int(input("Début: "))
f = int(input("Fin: "))
p = int(input("Pas: "))
for c in range(i, f+1, p):
    print(c)
print("FIN")

print("------------------")

for c in range(0, 3):
    num = int(input("Entrez un nombre: "))
print("Fim")

print("------------------")

somme = 0
for c in range(0, 4):
    nombre = int(input("Entrez un nombre: "))
    somme += nombre
print("La somme de tous les montants est {}".format(somme))
