from rich import print
class Funcionario:
    '''

    '''
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor= setor
        self.cargo = cargo
    def apresentar(self) -> str:
        return f':handshake: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo}, do setor de {self.setor} da empresa Curso em video'

c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentar())

c2 = Funcionario("João", "TI", "Programador")
print(c2.apresentar())