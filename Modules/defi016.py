#diviser et avoir la partie entier d'un nombre:
print("exemple 1")
import math
nombre = float(input("Informez un nombre: "))
print("Le numéro choisi est {} et sa partie entier est {}".format(nombre, math.trunc(nombre)))

print("#exemple 2")
from math import trunc
nombre  = float(input("Informez un nombre: "))
print("Le numéro choisi est {} et sa partie entier est {}".format(nombre, trunc(nombre)))

print("#exemple 3")
nombre = float(input("Informez un nombre: "))
print("Le numéro choisi est {} et sa partie entier est {}".format(nombre, int(nombre)))