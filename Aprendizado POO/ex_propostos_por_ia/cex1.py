class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def vender(self, qtd):
        if qtd <= 0:
            return 'Quantidade inválida'
        if qtd > self.estoque:
            return (f'Não é possível vender o produto {self.nome}, '
                    f'quantidade escolhida é maior do que o estoque')

        self.estoque -= qtd
        return f'Venda de {qtd} {self.nome}s bem sucedida'
    def repor(self, qtd):
        if qtd <= 0:
            return 'Quantidade inválida'
        self.estoque += qtd
        return f'A reposição de {qtd} {self.nome} foi realizado com sucesso'
    def mostrar_dados(self):
        return f'O estoque possui um total de {self.estoque} do produto {self.nome} no valor de R${self.preco}'

p1 = Produto('Refrigerante', 12, 5)
print(p1.vender(-4))
print (p1.repor(-10))
print (p1.mostrar_dados())


