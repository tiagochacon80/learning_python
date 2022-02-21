cote1 = int(input("Entrez le premier côté: "))
cote2 = int(input("Entrez le deuxième côté: "))
cote3 = int(input("Entrez le troisième côté: "))

if (cote1 < cote2 + cote3) and (cote2 < cote1 + cote3) and (cote3 < cote1 + cote2):
    print("Il forme un tringle")
    if (cote1 == cote2) and (cote2 == cote3):
        print("Triangle equilataire")
    else:
        if (cote1 == cote2) or (cote1 == cote3) or (cote2 == cote3):
            print("Triangle isosceles")
        else:
            if (cote1 != cote2) and (cote1 != cote3) and (cote2 != cote3):
                print("triangle escaleno")
else:
    print("Il ne forme pas en triangle")