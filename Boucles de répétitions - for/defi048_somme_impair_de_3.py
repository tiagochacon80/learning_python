#Écrivez un programme qui calcule la somme de tous les nombres multiples de trois et compris entre 1 et 500.
cont = 0
somme = 0 #acumulateur
'''
for c in range(1, 501):
    if c % 2 == 1: #Trouver le nombre impair
        if c % 3 == 0: #Trouver le multiple de 3
             print(c, end=" ")
             cont = cont + 1
             somme = somme + c '''
for c in range(1, 501, 2):
    #if c % 3 == 0:
     cont += 1
     somme += c
     print(c)
print()
print(f"La somme de tous les {cont} valeurs demandés est {somme}")

