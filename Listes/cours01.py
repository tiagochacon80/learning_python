num = [2, 5, 9, 1]
num[2] = 8 #Alterando o numero da posiçao [2] da lista por um valor externo = 8
num.append(7) #Adicionando valor e uma posiçao ao final da lista
num.sort() #Colocando os numeros da lista em ordem #Para inverter o numero seria, num.sort(reverse=True)
num.insert(2, 2)#Adicionando valor 0 na posiçao 2
#num.pop(2)#Elimina o valor da ultima posiçao, para selecionar uma posiçao a ser eliminada, basta adicionar a posiçao a ser eliminada desse jeito (2)
if 4 in num: #O uso do in nesse bloco faz toda diferença, ele da a condiçao para procurar o numero dentro da nossa lista
    num.remove(4)
else:
    print("Nao achei o numero 4")
num.remove(2)#Ele ira eliminar apenas o primeiro numero da lista, se tiver um outro numero igual, ele nao remove
print(num)
print(f"Essa lista tem {len(num)} elementos")
