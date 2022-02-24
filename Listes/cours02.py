valores = []
for cont in range(0, 2):
    valores.append(int(input("Digite um valor: ")))#Adicionar valores toda vez que o usuario digitar

for c, v in enumerate(valores):#Mostrando os valores sem os []
    print(f"Na posiçao {c} encontrei o valor {v}")

print()

a = [2, 3, 4, 7]
b = a #Aqui voce nao faz uma copia da primeira lista, voce faz uma ligaçao entre uma lista e outra
b[2] = 8 #O numero 8 sera adicionado nas duas listas, o python cria uma ligaçao entre as duas listas
print(f"Lista A: {a}")
print(f"Lista B: {b}")

a = [5, 9, 10, 11]
b = a[:]# Aqui ele iria criar uma copia da lista
b[2] = 8# Na copia ele ira trocar o valor da posiçao [2]
print(f"Lista A: {a}")
print(f"Lista B: {b}")