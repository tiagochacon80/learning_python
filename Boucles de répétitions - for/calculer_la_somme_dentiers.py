     #Calculer de la somme des n premiers entiers
n = int(input("Entrez un nombre n: "))
somme = 0
for i in range(1, n + 1): #(1,2,3...,n) O mais 1 (+1) é para pegar o ultimo numero, senao ele iria somar até o penulitmo
    somme = somme + i
print("La some des n premiers entiers vaut", somme)



