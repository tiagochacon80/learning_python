#Refaire DEFI 009, montrant la table de multiplication d'un nombre que l'utilisateur choisit, seulement maintenant en utilisant une boucle for.
nombre = int(input("Entrez un nombre pour la table de multiplication: "))
print("#####Version 1#####")
for c in range(1, 11):
    print(f"{nombre} x {c} = {nombre * c}")

print("#####Version 2#####")
nombre2 = int(input("Entrez un nombre pour la table de multiplication: "))
multi = 0
for c in range(1, 11):
    multi = nombre2 * c
    print(f"{nombre2} x {c} = {multi}")



