#Écrivez un programme qui calcule la somme de tous les nombres multiples de trois et compris entre 1 et 500.
cont = 0
somme = 0 #acumulateur
for c in range(1, 501, 2):
      if c % 3 == 0:
         print(c, end=" ")
         cont = cont + 1
         somme = somme + c
print()
print(f"La somme de tous les {cont} valeurs demandés est {somme}")

