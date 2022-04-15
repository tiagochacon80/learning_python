class CalcCube:
    """Classe qui permet calculer le cube d'un numéro"""
    def __init__(self, valeur):
        self.x = valeur
        print("Objet créé!")
    def calcule_cube(self):
        self.cube = self.x * self.x * self.x
        return f"Le cube de {self.x} = {self.cube}"

num = int(input("Entrez le premier numéro: "))
objCube = CalcCube(num) #instancier la classe
cube = objCube.calcule_cube()
num = int(input("Entrez le deuxième numéro: "))
objCube2 = CalcCube(num) #instancier la classe
cube2 = objCube2.calcule_cube()
print(cube)
print(cube2)
    





