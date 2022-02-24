cote1 = int(input("Entrez le premier nombre: "))
cote2 = int(input("Entrez le deuxième nombre: "))
cote3 = int(input("Entrez le troisième nombre: "))

if(cote1 < cote2 + cote3) and (cote2 < cote3 + cote1) and (cote3 < cote1 + cote2):
    print("Les nombres entrés peuvent former un triangle")
    if cote1 == cote2 and cote2 == cote3:
        print("Un triangle equilatero")
    elif (cote1 != cote2) and (cote2 != cote3) and (cote3 != cote1):
        print("Un triangle escaleno")
    else:
        print("Un triangle isosceles")
else:
    print("Les nombres ne peuvent pas former un triangle")