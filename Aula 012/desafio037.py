#Calculateur de nombres décimaux à binaires

decimal = int(input("Entrez un numéro: "))
binario = 0

i = 0
while (decimal > 0):
    digito = decimal % 2
    decimal = int(decimal // 2)
    binario = binario + digito*(10**i)
    i = i + 1
print(decimal , "en binaire = " , binario)




