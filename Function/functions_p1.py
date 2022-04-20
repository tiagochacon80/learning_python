n1 = 5
n2 = 10
def somar():
    r = n1 + n2
    print(f"A soma de {n1} + {n2} = {r}")

def subtrair():
    r = n2 - n1
    print(f"A subtraçao de {n2} - {n1} = {r}")

def multiplicar():
    r = n1 * n2
    print(f"A multiplicaçao de {n1} x {n2} = {r}")

def calculos():
    somar()
    subtrair()
    multiplicar()

calculos()