#Jeu de devinette
from random import randint
from time import sleep
print("-=-" * 21)
print("Je vais penser à un numéro entre 0 a 5, essayez de deviner...")
print("-=-" * 21)
numero = int(input("Quel numéro j'ai pensé? "))
print("EN TRAITEMENT, VEUILLEZ PATIENTER...")
sleep(2)
numero_ordi = randint(0, 5) #function pour selectionner un nombre aléatoire
if numero == numero_ordi:
    print("Felicitation!!! Vous avez reussi!!!")
else:
    print("Ce n'était pas cette fois, réessayez à nouveau.")
