class Mídia:
    def __init__(self, video):
        self.video=video
    def aparecer_na_tela(self):
        print(f"(self.video) está sendo exibido")

class Musica(Mídia):
    def __repr__(self):
        return f"'{self.titulo}' por {self.artista}"

class Playlist:
    def __init__(self, nome: str, musicas: list[Musica]):
        self.nome = nome
        self.musicas=musicas

    def tocar_todas(self):
        print(f"\n▶️ Tocando a playlist  '{self.nome}':")
        for musica in   self.musicas:
            print(f" - Tocando agora: {musica}")

    musica_1 = Musica("Toxicity", "System Of A Down")
    musica_2 = Musica("she", "Green Day")   
    musica_3 = Musica( "Sweet Child O' Mine","Guns n' Roses")
                      
daylist = Playlist("Sua playlist diária", 
                   [Musica_1, Musica_2, Musica_3])
daylist.tocar_todas()
    
