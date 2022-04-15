class Cube:
    '''Classe pour calculer le cube d'un numéro'''
    def __init__(self, valeur):  #méthode construteur
        self.x = valeur
        print("Objet créé!")
    def calcule_cube(self):
        cube = self.x * self.x * self.x
        return "Cube calculé " + str(cube)

test = Cube(6)
c = test.calcule_cube()
print(c)


