from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def calcular_valor_final(self, total):
        pass

    @abstractmethod
    def descricao(self):
        pass


class AVista(Pagamento):
    def __init__(self, desconto=0.05):
        self.desconto = desconto

    def calcular_valor_final(self, total):
        return total * (1 - self.desconto)

    def descricao(self):
        return f"À vista ({self.desconto:.0%} de desconto)"


class Parcelado(Pagamento):
    def __init__(self, parcelas, acrescimo_por_parcela=0.02):
        self.parcelas = parcelas
        self.acrescimo_por_parcela = acrescimo_por_parcela

    def calcular_valor_final(self, total):
        return total * (1 + self.acrescimo_por_parcela * self.parcelas)

    def descricao(self):
        return f"Cartão em {self.parcelas}x ({self.acrescimo_por_parcela:.0%} por parcela)"
