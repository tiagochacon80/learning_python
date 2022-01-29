#Faire un programme que lit un numéro et calcule le double, le triple et la racine carrée
numero = int(input("Entrez un numero: "))
double = numero * 2
triple = numero * 3
racine = numero ** (1/2)
print('Le numéro est {}, son double est {}, son triple est {}, la racine carrée est {}'.format(numero, double, triple, racine))