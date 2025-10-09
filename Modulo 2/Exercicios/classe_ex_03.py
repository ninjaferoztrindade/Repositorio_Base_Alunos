class Pessoa:
    def __init__(self, nome, peso, altura, gênero, hobbie, comida_favorita, etnia, roupa_preferida, o_que_está_fazendo, cabelo):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.gênero = gênero
        self.hobbie = hobbie
        self.comida_favorita = comida_favorita
        self.etnia = etnia
        self.roupa_preferida = roupa_preferida
        self.o_que_está_fazendo = o_que_está_fazendo 
        self.cabelo = cabelo 

    def fazer_som(self):
        print (f"O meu nome é {self.nome}")

    def pesar(self):
        print(f"{self.nome} 10 quilos.")
   
    def medir_altura(self):
        print(f"{self.nome} 90cm.")
    
    def dizer_gênero(self):
        print(f"{self.nome} masculino.")

    def dizer_hobbie(self):
        print(f"{self.nome} Bater em nerds.")

    def dizer_comida_favorita (self):
        print(f"{self.nome} Krusty Burger.")
    
    def dizer_etnia (self):
        print(f"{self.nome} amarelo.")
    
    def dizer_roupa_preferida (self):
        print(f"{self.nome} Camiseta_vermelha_short_azul.")    
    
    def dizer_o_que_está_fazendo (self):
        print(f"{self.nome} travessuras.")

    def dizer_o_tipo_do_cabelo (self):
        print(f"{self.nome} liso.")                     

p_e_s_s_o_a = Pessoa("bart","10 quilos", "90 cm", "masculino", "Bater em nerds", "Krusty Burger", "amarelo", "Camiseta_vermelha_short_azul", "travessuras", "liso")
p_e_s_s_o_a.fazer_som()
p_e_s_s_o_a.pesar()
p_e_s_s_o_a.medir_altura()
p_e_s_s_o_a.dizer_gênero()
p_e_s_s_o_a.dizer_hobbie()
p_e_s_s_o_a.dizer_comida_favorita()
p_e_s_s_o_a.dizer_etnia()
p_e_s_s_o_a.dizer_roupa_preferida()
p_e_s_s_o_a.dizer_o_que_está_fazendo()
p_e_s_s_o_a.dizer_o_tipo_do_cabelo()