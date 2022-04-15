class Chat:
    def __init__(self, nom):
        self.nom = nom
        print("Ton chat s'appelle", self.nom)

    def poids_chat(self, poids):
        self.poids = poids
        if self.poids >= 5.0:
            print("Voter chat est gros")
        elif self.poids > 3.5:
            print("Poid normal")
        else:
            print("L'animal est maigre")

    def _diete_especial_chat(self):
       self.msg = "Tout est normal"
       if self.poids < 3.5:
           self.msg = "augmenter la nourriture du animal"
       if self.poids >= 5.0:
           self.msg = "diminuer la norriture du animal"
       return self.msg

    def donnees_chat(self):
       print("\nLe chat", self.nom, "a", self.poids, "kg")
       print(self._diete_especial_chat())

nom_chat = input("entrez le nom de ton chat: ")
g1 = Chat(nom_chat)

poids = float(input("\nQuel est le poid de ton chat, en kg? "))
g1.poids_chat(poids)

g1.donnees_chat()
