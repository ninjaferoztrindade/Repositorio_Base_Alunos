
filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela", "Drive My Car", "A favorita" ],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle", "Big", "elf"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos", "A Lei é Para Todos", "DNA do Crime"],
    "guerra": ["Rambo","1917","Até o Último Homem","O Pianista", "A Vida é Bela", ],
    "terror": ["terrifier 1","terrifier 2","terrifier 3,","brinquedo assasino","corra",],
    "ação"  : ["missão impossivel","Bailarina: Do Universo de John Wick,", "Deadpool 2", "Shazam","Esquadrão Suicida"],
    "Ficção Científica" : ["Um Lugar Silencioso: Dia Um ", "Tudo em Todo Lugar ao Mesmo Tempo", "Duna ","Distrito 9", "Alien, o Oitavo Passageiro"],
    "animação" : ["Toy Story: Um Mundo de Aventuras","Detona Ralph", "Frozen", "Rio", "Os Simpsons - O Filme" ],
   "fantásia" : ["A Família Addams", "A Fantástica Fábrica de Chocolate", "Peter Pan", "Matilda", "A Menina e o Porquinho"],
    "Suspence" : ["Lobisomem ","Acompanhante Perfeita","Código Preto", "Pecadores","Last Breath"],
}   
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()