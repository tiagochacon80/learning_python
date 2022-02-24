from random import randint

print("Bienvenu au jeu de devinette!")
print("*********************************")

nombre_secret = randint(1, 100)
tentatives = 0
points = 1000

print("Voici les niveaux de difficultés")
print("(1) Facile (2) Moderé (3) difficile")

niveau = int(input("Choisissez votre niveau: "))

if niveau == 1:
    tentatives = 8
elif niveau == 2:
    tentatives = 5
else:
    tentatives = 3

for tour in range(1, tentatives + 1):
    print("Tour {} de {}".format(tour, tentatives))

    chute = int(input("Entrez un nombre entre 1 et 100: "))

    if(chute < 1 or chute > 100):
        print("Nombre invalide, tapez de 1 a 100")
        continue

    acertou = chute == nombre_secret
    maior = chute > nombre_secret
    menor = chute < nombre_secret

    if(acertou):
        print("Parabéns voce acertou e fez {} pontos".format(points))
        break
    else:
        points_perdu = abs(nombre_secret - chute)
        points = points - points_perdu
        if(menor):
            print("Errou!!! O numero é maior que", chute)
            if tour == tentatives:
                print("Le nombre secret était {}. Votre total des points est de {}".format(nombre_secret, points))
        elif(maior):
            print("Errou!!! O numero é menor que", chute)
            if tour == tentatives:
                print("Le nombre secret était {}. Votre total des points est de {}".format(nombre_secret, points))

print("Fin du jeu, vous avez épuisés toutes les tentatives")
