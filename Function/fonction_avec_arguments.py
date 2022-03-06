print("Version 1")
def addition(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"L'addition {a} + {b} = {s}")

addition(a=8, b=7)#On peut faire des échanges entre les valuers

print()
print("Version 2")
def addition(a, b):
    return a + b

print(addition(20, 15))

print()
print("Version 3")
valeur = [1, 2, 3, 4, 5]

def carree(valeur):
    carrees = []
    for x in valeur:
        carrees.append(x**2)
    return carrees

resultats = carree(valeur)

for y in resultats:
    print(y)







