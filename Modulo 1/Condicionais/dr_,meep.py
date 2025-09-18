def raças_cachoros ():
    valor_total= 0
    raça = input ("Digite uma raça")
    raças = ['pug','pastor-alemão', 
         'labrador']
    if raça in raças: 
        if raça == 'pug':
         valor_total = 70.99
        print(valor_total)
    elif raça == 'pastor-alemão':
     valor_total= 120.99
     print (valor_total)   
    else:
       print("atendimento não disponivel")
raças_cachoros()    
