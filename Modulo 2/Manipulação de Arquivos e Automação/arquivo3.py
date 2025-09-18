import os
#os.getcwd()

import os
#os.mkdir("d")
#os.mkdir("e")
#os.mkdir("f")

import os

try:
   
    for n in range(1,51):
        os.mkdir("pasta_%d" % n)
    os.chdir("pasta_1")   
    arquivo=open("arquivo_1.tx", "w")
    arquivo.write("oi")
    arquivo.close()
except FileNotFoundError:   
    print('arquivo não encontrado!')

try:
    arquivo=open("números.txt", "w")
    for linha in range(1,101):
        arquivo.write("%dnãotoentendendo\n" % linha)
    arquivo.close()   
except FileNotFoundError:
    print ('Arquivo não encontrado!')    
