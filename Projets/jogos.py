import forca
import jogo_adivinhacao

print("*"*27)
print("****Escolha o seu jogo!****")
print("*"*27)

print("(1) Forca (2) Devinette")

jeu = int(input("Quel jeu vous voulez jouer? "))

if jeu == 1:
    print("Jouer forca")
    forca.jouer()
elif jeu == 2:
    print("Jouer devinette")
    jogo_adivinhacao.jouer()