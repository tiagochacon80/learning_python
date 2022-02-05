#Tire un nom de la liste
import random
nom1 = input("Premier nom ")
nom2 = input("Deuxième nom ")
nom3 = input("Troisième nom ")
nom4 = input("Quatrième nom ")
liste = [nom1, nom2, nom3, nom4]
tirage = random.choice(liste)
print("Le nom tiré est {}".format(tirage))