class Categoria:
    def __init__(self, nome, comissao):
        self.nome = nome
        self.comissao = comissao


class Produto:
    def __init__(self, nome, categoria, preco, estoque, garantia_meses):
        self.nome = nome
        self.categoria = categoria
        self.garantia_meses = garantia_meses
        self.__preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    def alterar_preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("Preço inválido")
        self.__preco = novo_preco

    def repor_estoque(self, quantidade):
        self.__estoque += quantidade

    def baixar_estoque(self, quantidade):
        if quantidade > self.__estoque:
            raise ValueError(f"Estoque insuficiente de {self.nome}")
        self.__estoque -= quantidade

    def detalhes(self):
        return f"Garantia: {self.garantia_meses} meses"


class LinhaBranca(Produto):
    def __init__(self, nome, categoria, preco, estoque, garantia_meses, consumo_kwh, eficiencia):
        super().__init__(nome, categoria, preco, estoque, garantia_meses)
        self.consumo_kwh = consumo_kwh
        self.eficiencia = eficiencia

    def detalhes(self):
        return f"{super().detalhes()} | {self.consumo_kwh} kWh/mês | Eficiência {self.eficiencia}"


class Eletroportatil(Produto):
    def __init__(self, nome, categoria, preco, estoque, garantia_meses, voltagem):
        super().__init__(nome, categoria, preco, estoque, garantia_meses)
        self.voltagem = voltagem

    def detalhes(self):
        return f"{super().detalhes()} | Voltagem {self.voltagem}"
