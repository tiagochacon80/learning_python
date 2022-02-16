from random import randint

print("Bienvenu au jeu de devinette!")
print("*********************************")

nombre_secret = randint(1, 100)
tentatives = 4
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
    print("Rodada {} de {}".format(tour, tentatives))
    chute = int(input("Digite o seu numero entre 1 e 100: "))
    if(chute < 1 or chute > 100):
       print("Numero invalido, digite de 1 a 100")

    acertou = chute == nombre_secret
    maior = chute > nombre_secret
    menor = chute < nombre_secret

    if(acertou):
        print("Parabéns voce acertou e fez {} pontos".format(points))
        break
    else:
        if(menor):
            print("Errou!!! O numero é maior que", chute)
        elif(maior):
            print("Errou!!! O numero é menor que", chute)
        points_perdu = abs(nombre_secret - chute)
        points = points - points_perdu

    tour = tour + 1

    print("Fim do jogo, voce esgotou todas as tentativas")
