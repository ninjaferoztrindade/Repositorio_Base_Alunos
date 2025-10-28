import sqlite3

try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor () # abrindo cursor
    # cur.execute("CREATE TABLE pessoa(id, nome, idade, cpf)")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(1, 'Thiago', 35, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(2, 'Arthur', 54, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(3, 'Luiz', 18, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(4, 'Gabriela', 78, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(5, 'Mateus', 21, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(6, 'Roberto', 49, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(7, 'Hugo', 81, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(8, 'Henrique', 19, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(9, 'João', 67, '214.112.756.34')")# criando tabela pessoa 
    # cur.execute("INSERT INTO pessoa VALUES(10, 'Enzo',91, '214.112.756.34')")# criando tabela pessoa
    # cur.execute("DELETE FROM pessoa WHERE id = 5")
    res=cur.execute("SELECT * FROM pessoa Nome = 'Mateus'")
    con.commit()

except ConnectionRefusedError as c:
    print ('Erro de conexão com o banco.')    
