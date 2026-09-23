from produtos import Categoria, LinhaBranca, Eletroportatil
from pessoas import Cliente, Vendedor
from pagamento import AVista, Parcelado
from venda import Venda, Recibo
from estoque import Estoque

linha_branca = Categoria("Linha Branca", 0.03)
eletroportateis = Categoria("Eletroportáteis", 0.05)

geladeira = LinhaBranca("Geladeira Frost Free", linha_branca, 3200.00, 10, 12, 45, "A")
fogao = LinhaBranca("Fogão 5 Bocas", linha_branca, 1500.00, 5, 12, 20, "B")
liquidificador = Eletroportatil("Liquidificador", eletroportateis, 200.00, 20, 6, "bivolt")

estoque = Estoque()
for produto in (geladeira, fogao, liquidificador):
    estoque.cadastrar(produto)

vendedor = Vendedor("Carlos")
cliente = Cliente("Maria Silva", "123.456.789-00")

venda1 = Venda(vendedor, cliente, AVista())
venda1.adicionar_item(geladeira, 1)
venda1.adicionar_item(liquidificador, 2)
venda1.concluir(estoque)
print(Recibo.gerar(venda1))

venda2 = Venda(vendedor, cliente, Parcelado(6))
venda2.adicionar_item(fogao, 1)
venda2.concluir(estoque)
print()
print(Recibo.gerar(venda2))

print()
print("Estoque atual:")
for p in estoque.listar():
    print(f"{p.nome}: {p.estoque}")

print()
print(f"Comissão acumulada de {vendedor.nome}: R$ {vendedor.comissao_total:.2f}")

print()
print(f"Histórico de {cliente.nome}:")
for v in cliente.historico:
    print(f"- {len(v.itens)} item(ns) | R$ {v.valor_final:.2f} | {v.pagamento.descricao()}")
