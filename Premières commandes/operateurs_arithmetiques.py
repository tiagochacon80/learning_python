numero1 = int(input("Entrez le premier numero: "))
numero2 = int(input("Entrez le deuxième numero: "))

addition = numero1 + numero2
soustraction = numero1 - numero2
multiplication = numero1 * numero2
division = numero1 / numero2
divi_entiere = numero1 // numero2
reste = numero1 % 2
puissance = numero1 ** numero2

print("La somme est {}, la multiplication est {}, la division est {:.2f}".format(addition, multiplication, division))
print("La division entiere est {}, la pauissance est {} et le reste est {}".format(divi_entiere, puissance, reste))
