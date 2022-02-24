from random import randint
from time import sleep
item = ('ROCHE', 'PAPIER', 'CISEAUX')
print('''Vos options: 
[0] ROCHE
[1] PAPIER
[2] CISEAUX''')

joueur = int(input("Quel est votre choix: "))
if joueur > 2 or joueur < 0:
    print("Numéro invalide")
else:
    print("*"*29)
    print(f"Joueur a choisi {item[joueur]}")
    ordinateur = randint(0, 2)
    print(f"L'ordinateur a choisi {item[ordinateur]}")
    print("*"*29)
    print("Traitement en cours...")
    sleep(1)
    if joueur == 2 and ordinateur == 0:
       print("l'ordinateur gagne!")
    elif ordinateur == 2 and joueur == 0:
       print("Le joueur gagne")
    elif joueur > ordinateur:
       print("Le joueur gagne")
    elif ordinateur > joueur:
       print("L'ordinateur gagne")
    elif joueur == ordinateur:
       print("Égalité")

