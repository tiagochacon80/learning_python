premier = int(input("Entrez le premier nombre: "))
deuxieme = int(input("Entrez le deuxième nombre: "))
troisieme = int(input("Entrez le troisième nombre: "))

plus_grand = premier
if deuxieme > premier and deuxieme > troisieme:
    plus_grand = deuxieme
if troisieme > premier and troisieme > deuxieme:
    plus_grand = troisieme

plus_petit = premier
if deuxieme < premier and deuxieme < troisieme:
    plus_petit = deuxieme
if troisieme < premier and troisieme < deuxieme:
    plus_petit = troisieme

#méthode la plus simple
#plus_petit = min(premier, deuxieme, troisieme)
#plus_grand = max(premier, deuxieme, troisieme)

print("Le nombre plus petit est: {}".format(plus_petit))
print("Le nombre plus grand est: {}".format(plus_grand))


