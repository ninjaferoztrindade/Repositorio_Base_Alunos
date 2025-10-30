--Sistema de Biblioteca
CREATE TABLE IF NOT EXISTS livro (
    idLivro             INTEGER,
    genêro              Varchar(50),
    titulo              Varchar(50),
    dataPublicitário    DATE,
    autor               VARCHAR(200),
); 

CREATE TABLE IF NOT EXISTS aluno (
    idAluno                 INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                    VARCHAR(255),
    celular                 VARCHAR(15),
    turma                   CHAR(1)
);

CRATE TABLE IF NOT EXISTS emprestimo (
    idEmprestimo        INTEGER  PRIMARY KEY AUTOINCREMENT
    VALOR               REAL,
    idLivro             INTEGER,
    FOREIGN KEY     (idAluno)   REFERENCES  aluno(idAluno),
    FOREIGN KEY     (idLivro)   REFERENCES  livro(idLivro)

);

