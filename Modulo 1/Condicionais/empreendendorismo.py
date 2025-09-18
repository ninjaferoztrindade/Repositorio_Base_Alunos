estoque= {"celulares": [500,1500],
          "tablet": [200,99],
          "notebook":[30,1800],  
          "smartwath":[20,1999], 
          "Teclados":[10,55.30], 
          "mouses": [10,33.90], 
          "video game":[10,98.5000],              
          "caixas de som":[10,33.21],
          "sanduicheiras":[54,100],
          "televisores":[99,211],
          "fone":[88,99],
          "pen drive":[500,20],
          "monitor": [90,200],
          "HD externo": [32,250],
          "impressora": [55,600],
          "drone": [10,300],
          "camerâ digital": [30,70],      
          "projetor": [72,500],
          "placa de video": [20, 3000],
          "Fonte de alimentação": [30,60],
           "Gravador de voz digital": [10,40]}
sei_lá_oque = input("Digite o produto: ")
venda = [ [sei_lá_oque, int(input("Digite a quantidade: ")) ] ] 
     
total = 0
print("Vendas:\n")
if sei_lá_oque in estoque:
  for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:    
  print("insufissiente!")
print("Custo total : %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados [1])    


