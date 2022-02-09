#Un programme qui lit un nombre de 0 a 9999 et affiche chaqu'un des chiffres séparé
nombre = int(input("Entrez un numéro: "))
unite = nombre // 1 % 10
dizaine = nombre // 10 % 10
centaines = nombre // 100 % 10
milliers = nombre // 1000 % 10
print("Analyse du numéro: {}".format(nombre))
print("Unité: {}".format(unite))
print("Dizaines: {}".format(dizaine))
print("Centaines: {}".format(centaines))
print("Milliers: {}".format(milliers))