def banco_Brasil():
    saldo = int(input("Digite o saldo bancário"))
    saque = int(input("Digite o valor de saque"))
    if saldo >=saque:
        saldo -= saque
        print ("Você realizou um saque com sucesso.", saldo)
    else:
        print("Você não possui saldo suficiente para realizar essa operação", saldo)
#banco_Brasil()
print("-------------x-------------")
def depósito_dinheiro():
    saldo = int(input("deposite o valor depositado"))
    deposito =int(input("deposite o deposito de dinheiro"))
    saldo += deposito
    print("o deposito de dinheiro foi realizado com sucesso", saldo)
depósito_dinheiro()
def porcentagem():
    valor_parte= float(input("insira o valor parte:"))
    porcentagem = float(input("insira o valor da porcentagem: "))
    valor_total = valor_parte * (porcentagem/100)
    print(valor_total)
if porcentagem <=0.0:
    print("insira  um numero maior que 0")
else:
    print("insira um numero menor que 0")


    
            
