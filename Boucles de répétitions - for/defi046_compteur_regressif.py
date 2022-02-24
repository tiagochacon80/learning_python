#Écrivez un programme qui affiche un compte à rebours jusqu'à l'éclatement des feux d'artifice sur l'écran, allant de 10 à 0, avec une pause de 1 seconde entre eux.
import time
for c in range(10, - 1, -1):
    time.sleep(0.5)
    print(c)
print("BUUUUMMMM!!!")
