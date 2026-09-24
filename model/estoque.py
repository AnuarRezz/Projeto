class Estoque:
    def __init__(self):
        self.__produtos = []

    def cadastrar(self, produto):
        self.__produtos.append(produto)

    def listar(self):
        return list(self.__produtos)

    def baixar(self, itens):
        for item in itens:
            if item.quantidade > item.produto.estoque:
                raise ValueError(f"Estoque insuficiente de {item.produto.nome}")
        for item in itens:
            item.produto.baixar_estoque(item.quantidade)
