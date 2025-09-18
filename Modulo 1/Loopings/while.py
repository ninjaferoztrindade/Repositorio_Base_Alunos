def tabuada ():
    n = int(input("Tabuada de :"))
    x = 1 
    while x <= fim:
        print(n,"x",x,"=",x*n)
    x=x+1
print("-----------x-----------")
def whilebreak():
    s=0
    while True:
        v =int(input("Digite um número a somar ou 0 para sair:"))
        if v==0:
            break
        s = s+v
    print(s)                        
whilebreak()
