     #Calculer de la somme des n premiers entiers
n = int(input("Entrez un nombre n: "))
somme = 0
for i in range(1, n + 1): #(1,2,3...,n)
    somme = somme + i
print("La some des n premiers entiers vaut", somme)



