#Créez un programme qui affiche à l'écran tous les nombres pairs compris entre 1 et 50.
print("Version 1")
for c in range(2, 51, 2):
    print(c, end=" ")
print("Terminé")

print("Version 2")
for n in range(2, 51):
    if n % 2 == 0:
        print(n, end=" ")
print("Terminé")
