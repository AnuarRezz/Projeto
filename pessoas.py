class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.__historico = []

    @property
    def historico(self):
        return list(self.__historico)

    def registrar_venda(self, venda):
        self.__historico.append(venda)


class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.__comissao_total = 0

    @property
    def comissao_total(self):
        return self.__comissao_total

    def registrar_comissao(self, valor):
        self.__comissao_total += valor
