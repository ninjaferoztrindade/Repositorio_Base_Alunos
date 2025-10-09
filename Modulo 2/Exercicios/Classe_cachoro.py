from Classe_pai import Animal

class Cachoro(Animal):
    def __init__(self, nome, raca):

        super().__init__(nome)
        self.raca = raca
    def fazer_som(self):
        print (f"{self.nome} está latindo:Au Au!")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo.") 
    def abanar_rabo(self):
        print(f"{self.nome} está cagando.")
    def abanar_rabo(self):
        print(f"{self.nome} está brincando.")         


animal_raça_nome = Cachoro("ajudante de papai noel","greyhound")
animal_raça_nome.comer()
animal_raça_nome.abanar_rabo()
animal_raça_nome.fazer_som()
      