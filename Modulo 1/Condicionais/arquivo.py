try:
    arquivo=open("números.txt", "w")
    for linha in range(1,101):
        arquivo.write("%dnãotoentendendo\n" % linha)
    arquivo.close()   
except FileNotFoundError:
    print ('Arquivo não encontrado!')                