--Sistema do jogo

CREATE TABLE IF NOT EXISTS Skins (
    idskin        INTEGER,
    nome           VARCHAR(255)   
);

CRATE TABLE IF NOT EXISTS Itens (
    idItem             INTEGER  PRIMARY KEY AUTOINCREMENT
    idEspecie          INTEGER,
    Função             VARCHAR(255)

);    

CRATE TABLE IF NOT EXISTS Personagens (
    idPersonagem        INTEGER  PRIMARY KEY AUTOINCREMENT
    Habilidade          VARCHAR(255),     
    genero              VARCHAR(255)             
);    


CRATE TABLE IF NOT EXISTS Mapa (
    idskin        INTEGER  PRIMARY KEY AUTOINCREMENT                  
    idPersonagem  INTEGER, PRIMARY KEY AUTOINCREMENT

);    


CRATE TABLE IF NOT EXISTS Temporada (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    nome          VARCHAR(255),
    idskin        INTEGER,                   
    idPersonagem  INTEGER,
    idItem        INTEGER,
    FOREIGN KEY idskin REFERENCES Skins(idskin),
);   

CREATE TABLE IF NOT EXISTS Jogo (
    id             INTEGER,
    genêro             Varchar(50),
    item               Varchar(50),
    titulo             Varchar(50),
    personagens        Varchar(50),
    mapa               Varchar(50)    
    skins              Varchar(50)
    idTemporada         INTEGER,
    FOREIGN KEY idTemporada REFERENCES Temporada(id),
    
); 

CREATE TABLE IF NOT EXISTS Jogadores (
    idJogador                 INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                    VARCHAR(255),
    usuário                 VARCHAR(255),                 
                            CHAR(1)
    FOREIGN KEY     (idItens)   REFERENCES  Itens(idItem),
    FOREIGN KEY     (idPersonagens)   REFERENCES  Personagens(idPersonagem)
);


