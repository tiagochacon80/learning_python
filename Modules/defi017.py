#Triangle rectangle - hypotenuse formule a² + b² = c²
print("Solution #1")
ca = float(input("Cathète plus grand: "))
co = float(input("Cathète plus petit: "))
hypoteneuse = (co ** 2 + ca ** 2) ** (1/2)

print("L'hypoteneuse ira mesuré {:.2f}".format(hypoteneuse))

print()
print("Solution #2 - module")
import math
ca = float(input("Cathète plus grand: "))
co = float(input("Cathète plus petit: "))
print("L'hypoteneuse est de {:.2f}".format(math.hypot(ca, co)))

