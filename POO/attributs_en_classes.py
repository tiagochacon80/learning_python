class Chat:
    #attribut de classe
    type_animal = "Félin"

    def __init__(self, nom):
        #variable d'instance
        self.nom = nom

#changement de variable de classe
Chat.type_animal = "Pet"

#creation d'objet
g1 = Chat("Zeus")
g2 = Chat("Atena")

print(g1.type_animal)
print(g2.type_animal)

print(g1.nom)
print(g2.nom)

#changement de variable d'instance
g1.type_animal = "chatte"
print(g1.type_animal)
print(g2.type_animal)


        