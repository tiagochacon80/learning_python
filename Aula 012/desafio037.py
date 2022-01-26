#Calculateur de nombres décimaux à binaires

decimaux = int(input("Entrez un numéro: "))
binaire = 0

i = 0
#decimaux = 15
while (decimaux > 0): #15 > 0 | 7 > 0 | 3 > 0 | 1 > 0
    reste = decimaux % 2 #reste = 15 % 2 = 1 | reste = 7 % 2 = 1 | 3 % 2 = 1 | 1 % 2 = 1
    decimaux = decimaux // 2 #decimaux = 15 // 2 = 7 | 7 // 2 = 3 | 3 // 2 = 1 | 1 // 2 = 0
    binaire = binaire + reste*(10**i) # binaire = 0 + 1 * (10**0) = 0 + 1 = 1 | 1 + 1 * (10**1) = 1 + 1 * 10 = 11 | 11 + 1 * (10**2) = 11 + 1 * 100 = 111 | 111 + 1 * (10**3) = 111 + 1 * 1000 = 1111
    i = i + 1 #i = 0 + 1 = 1 | 2 | 3 | 4
print(decimaux , "en binaire = " , binaire)




