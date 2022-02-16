from random import randint

print("Bienvenu au jeu de devinette!")
print("*********************************")

numero_secreto = randint(1, 100)
tentativas = 4
points = 1000

print("Voici les niveaux de difficultés")
print("(1) Facile (2) Moderé (3) difficile")

niveau = int(input("Choisissez votre niveau: "))

if niveau == 1:
    tentativas = 8
elif niveau == 2:
    tentativas = 5
else:
    tentativas = 3

for rodada in range(1, tentativas + 1):
    print("Rodada {} de {}".format(rodada, tentativas))
    chute = int(input("Digite o seu numero entre 1 e 100: "))
    if(chute < 1 or chute > 100):
       print("Numero invalido, digite de 1 a 100")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns voce acertou e fez {} pontos".format(points))
        break
    else:
        if(menor):
            print("Errou!!! O numero é maior que", chute)
        elif(maior):
            print("Errou!!! O numero é menor que", chute)
        points_perdu = abs(numero_secreto - chute)
        points = points - points_perdu

    rodada = rodada + 1

    print("Fim do jogo, voce esgotou todas as tentativas")
