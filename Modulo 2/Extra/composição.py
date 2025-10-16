class ItenDoPedido
    def __init__(self, produto: str, quantidade: int, preco_unitário: float):
        self.produto = produto 
        self.quantidade = quantidade 
        self.preco_unitario

    def calcular_subtotal(self)-> float:
        return self.quantidade * self.preco_unitario

class Pedido:
    def __init__(self, id_cliente: int):        
        self.id_cliente = id_cliente
        self.itens = id_cliente
        self._itens = []
        print(f"\nPedido criado pra o cliente {self.id_cliente}.")

    def adicionar_item(self, produto: str, quantidade: int, preco_unitario: float):
        novo_item = ItemDoPedido(produto, quantidade, preco_unitario)
        self._itens.append(novo_item)
        print(f"  - Item ' {produto}' adicionado ao pedido.")

    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self._itens)
        print(f"Total do pedido: R$ {total:.2f}")

    pedido_123 = Pedido(957)

    pedido_123.adicionar_item("Notebook Gamer ", 1, 5000.00)
    pedido_123.adicionar_item("Mouse sem fio", 2, 150.00)
    pedido_123.adicionar_item("Monitor", 6, 133.00)
    pedido_123.adicionar_item("Pen drive", 8, 166.00)
    pedido_123.adicionar_item("Teclado Mecânico", 3, 100.00)



