#Jeu de devinette
import random
print("Je vais penser a un numéro entre 0 a 5, essayez de deviner...")
numero = int(input("A quel numero j'ai pensé? "))
print("EN TRAITEMENT, VEUILLEZ PATIENTER...")
numero_ordi = random.randrange(0, 5) #function pour selectionner un nombre aléatoire
if numero == numero_ordi:
    print("Felicitation!!! Vous avez reussi!!!")
else:
    print("Ce n'était pas cette fois, réessayez à nouveau.")
