class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = produto.preco

    @property
    def subtotal(self):
        return self.preco_unitario * self.quantidade

    @property
    def comissao(self):
        return self.subtotal * self.produto.categoria.comissao


class Venda:
    def __init__(self, vendedor, cliente, pagamento):
        self.vendedor = vendedor
        self.cliente = cliente
        self.pagamento = pagamento
        self.concluida = False
        self.__itens = []

    @property
    def itens(self):
        return list(self.__itens)

    @property
    def total(self):
        return sum(item.subtotal for item in self.__itens)

    @property
    def valor_final(self):
        return self.pagamento.calcular_valor_final(self.total)

    @property
    def comissao(self):
        return sum(item.comissao for item in self.__itens)

    def adicionar_item(self, produto, quantidade):
        self.__itens.append(ItemVenda(produto, quantidade))

    def concluir(self, estoque):
        if self.concluida or not self.__itens:
            raise ValueError("Venda não pode ser concluída")
        estoque.baixar(self.__itens)
        self.vendedor.registrar_comissao(self.comissao)
        self.cliente.registrar_venda(self)
        self.concluida = True


class Recibo:
    @staticmethod
    def gerar(venda):
        linhas = [
            "===== CASA & CONFORTO - RECIBO =====",
            f"Cliente: {venda.cliente.nome}",
            f"Vendedor: {venda.vendedor.nome}",
            "-" * 37,
        ]
        for item in venda.itens:
            linhas.append(
                f"{item.quantidade}x {item.produto.nome} - R$ {item.subtotal:.2f}"
            )
            linhas.append(f"   {item.produto.detalhes()}")
        linhas += [
            "-" * 37,
            f"Total: R$ {venda.total:.2f}",
            f"Pagamento: {venda.pagamento.descricao()}",
            f"Valor final: R$ {venda.valor_final:.2f}",
        ]
        return "\n".join(linhas)
