def for_lista():
    L=(8,9,15,16,17,19,23,54,67,78,89,90,99)
    for thiago in L: 
        print(thiago)
print("---------x----------")    
def listas_frutas():
    frutas = ["maçãs","peras","kiwis","morango", "manga", "uva", "tangerina" ]
    for palavra in frutas:
        for letra in palavra:
         print(letra, end="_")
print("-x-x-x-x-x-x-x-x-x-")
def exibe_máximo():
    L=[1,7,2,4,-1,-2,-3,-9,-12,99]
    máximo=L[0]
    for e in L:
        if e > máximo:
            máximo = e
        print(máximo)
exibe_máximo()
print("--------x----")
def exibe_minimo():
    T=[312,234,564-321,-123]
    minimo=T[0]
    for e in L:
        if e > minimo:
            minimo = e
        print(minimo)

print("-----------x------------")   
for v in range(10):
    print(v) 
print("-------x------")
for v in range (5,8):
    print(v)
print("----------x----------")    
for t in range (3,33,3):
    print(t,end=" ")
    
    print ("------x---------")   
nome = "Thiago"
idade = 15
grana = 100000
print("%s tem %d anos e R$%f no bolso. " % (nome,idade,grana))
print("%12s tem %03d anos e R$%5.2f no bolso. " % (nome, idade, grana))
print("%-12s tem %-3d anos e R$%-5.2f no bolso. " % (nome,idade,grana))
