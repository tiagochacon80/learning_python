#Un programme qui lit un angle et affiche la valeur du sinus cosinus et tangente
import math
angle = int(input("Entrez avec un angle: "))
sinus = math.sin(math.radians(angle))
print("L'angle de {} a le sinus de {:.2f}".format(angle, sinus))
cosinus = math.cos(math.radians(angle))
print("L'angle de {} a le cosinus de {:.2f}".format(angle, cosinus))
tangente = math.tan(math.radians(angle))
print("L'angle de {} a la tangente de {:.2f}".format(angle, tangente))