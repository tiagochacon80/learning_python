class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia = 100
    def info(self):
        print("Nome:....." + self.nome)
        print("Time:....." + str(self.time))
        print("Força:...." + str(self.forca))
        print("Muniçao:.." + str(self.municao))
        print("Vivo:....." + ("sim" if self.vivo else "nao"))
        print("Energia..:" + str(self.energia))
        print("--------------------------------------")

    class Soldado(NPC):
        def __init__(self, nome, time):
            self.forca=200
            self.municao=200
            super().__init(nome, time, self.forca, self.municao)

    class Guarda(NPC):
        def __init__(self, nome, time):
            self.forca=100
            self.municao=10
            super().__init__(nome, time, self.forca, self.municao)