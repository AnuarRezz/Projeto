from estoque import Estoque
from pagamento import Pagamento
from pessoas import Cliente, Funcionario
from pessoas import Pessoa
from venda import Venda

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = Estoque()
        self.clientes = []
        self.funcionarios = []
        self.vendas = []

    def cadastar_produto(self, produto):
        self.estoque.adicionar_produto(produto)
    
    def registrar_venda(self, venda):
        self.vendas.append(venda)
        self.estoque.remover_produto(venda.produto)
    
    def forma_pagamento(self, venda):
        self.vendas

    def atualizar_estoque(self, produto, quantidade):
        self.estoque.atualizar_quantidade(produto, quantidade)
    
    def emitir_comprovante(self, registrar_venda):
        self.atualizar_estoque(produto, registrar_venda)
    
