#Calculateur de nombres décimaux à binaires

decimaux = int(input("Entrez un numéro: "))
binaire = 0

i = 0
while (decimaux > 0):
    reste = decimaux % 2
    decimaux = decimaux // 2
    binaire = binaire + reste*(10**i)
    i = i + 1
print(decimaux , "en binaire = " , binaire)




