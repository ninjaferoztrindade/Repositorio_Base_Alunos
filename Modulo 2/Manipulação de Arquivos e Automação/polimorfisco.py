x = " Olá, Mundo!"
print(len(x))

minha_tupla = ("Maçã","Banana","Cereja")
print(len(minha_tupla))

este_dicionário = {
    " marca": "Chevrolet",
    "modelo": "Opala",
    "ano"   : 1969
}
print(len(este_dicionário))
from ..Exercicios.Classe_pai import animal
animal1 = animal(23_000_000, "Megalodonte", 18.00, "rei dos rios tiete")
from ..Exercicios.Classe_pai import animais_marinhos
animal2 = animais_marinhos(70, "Crocodilo_Água_Salgada", "3 metros", "rei das águas salgadas")
from ..Exercicios.Classe_pai import passáro
animal3 = passáro(150_000_000 ,"Pterodactylus", 0.75, "rei dos passáros" )

def comunicar(qualquer_animal):
    print("tentando_comunicarr com (qualquer_animal.espécie)")
     
