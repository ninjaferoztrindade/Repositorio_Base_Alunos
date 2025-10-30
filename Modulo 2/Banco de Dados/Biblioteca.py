import sqlite3

try:
    con = sqlite3.connect('biblioteca.db')
    cur = con.cursor()

    cur.executescript("""
CREATE TABLE IF NOT EXISTS livro (
    idLivro             INTEGER PRIMARY KEY AUTOINCREMENT,
    genero              VARCHAR(50),
    titulo              VARCHAR(50),
    dataPublicacao      DATE,
    autor               VARCHAR(200)
); 

CREATE TABLE IF NOT EXISTS aluno (
    idAluno                 INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                    VARCHAR(255),
    celular                 VARCHAR(15),
    turma                   CHAR(1)
);

CREATE TABLE IF NOT EXISTS emprestimo (
    idEmprestimo        INTEGER  PRIMARY KEY AUTOINCREMENT,
    VALOR               REAL,
    idLivro             INTEGER,
    idAluno             INTEGER,
    FOREIGN KEY     (idAluno)   REFERENCES  aluno(idAluno),
    FOREIGN KEY     (idLivro)   REFERENCES  livro(idLivro)

);                                           

INSERT INTO aluno(nome, celular, turma)
VALUES
('Pedro Henrique', '12345678910', '1'),
('Joana Vieira'  , '12345678910', '1'),
('Miguel José'   , '12345678910', '1'),
('Thiago Gabriel', '12345678910', '1'),
('Victor Hugo'   , '12345678910', '1'),
('Guilherme'     , '12345678910', '1');

INSERT INTO 

livro (genero, titulo, dataPublicacao, autor)
VALUES('Terror', 'IT: A Coisa' , date('now'), 'Stephen King'),
('Comédia', 'Diário de um banana', date('now'),'Jeff Kinney'),
('Quadrinhos', 'Batman Absoluto', date('now'), ' Scott Snyder');

INSERT INTO emprestimo(valor, idLivro, idAluno)
VALUES
(30.00, 1, 3),
(7.00, 2, 6), 
(9.00,3,2);
""")
    con.commit()
    cur.close()
except ConnectionRefusedError as e:
    print('Erro de conexão: ', e)   