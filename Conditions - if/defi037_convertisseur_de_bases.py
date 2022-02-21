#Écrire un programme qui converti un nombre en binaire, octal ou hexadecimal
nombre = int(input("Entrez un nombre entier: "))
print('''Choisissez une des bases pour la conversion: ")
[1] conversion en binaire
[2] conversion en octal
[3] conversion en hexadecimal''')

option = int(input("Votre option: "))

if option == 1:
    print("{} converti en binaire est = {}".format(nombre, bin(nombre)[2:])) #[2:] On coupe la chaine et on supprime le deux premiers
elif option == 2:
    print("{} converti en octal est = {}".format(nombre, oct(nombre)[2:]))
elif option == 3:
    print("{} converti en hexadecimal est = {}".format(nombre, hex(nombre)[2:]))
else:
    print("Valeur incorrecte, entrez les valeurs [1], [2] ou [3]")

