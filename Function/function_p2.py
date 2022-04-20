def somar(n1, n2):  #fonction avec paramètres
    r = n1 + n2
    print(f"A soma de {n1} + {n2} = {r}")

somar(5, 7)
somar(8, 12)
somar(4, 10)

print()

def textos(*txt):
    for t in txt:
        print(t)

textos("Python", "Cours", "Ulaval", "informatique")

print()

valores = [1,2,3,4,5]
def somar(num):
    resul = 0
    for n in num:
        resul += n
    print(f"Soma = {resul}")

somar(valores)