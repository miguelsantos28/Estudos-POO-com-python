from rich import print
class Funcionario:

    def __init__(self, nome, setor, cargo, salario):
        self.nome = nome
        self.__setor= setor
        self.cargo = cargo
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario < 0:
            print("Salário inválido!")
            return

        self.__salario = novo_salario
    def apresentar(self) -> str:
        return f'\n:handshake: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo}, do setor de {self.__setor} da empresa Curso em video, recebo R${self.__salario :.2f}\n'

    def aumentar_salario(self, percentual):
        if percentual <= 0:
            return '\nPor favor, digite um percentual válido!\n'
        self.__salario += self.__salario * (percentual/100)
        return f'\nAumento de {percentual}% no salário de [bold blue]{self.nome}[/], realizado com sucesso\n'

    def trocar_setor(self, novo_setor):
        self.__setor = novo_setor
        return f'\nAlteração de setor realizada com sucesso no funcionário [bold blue]{self.nome}[/]\n'

    def mostrar_dados(self):
        return self.apresentar()



c1 = Funcionario("Maria", "Administração", "Diretora", 1500)
print(c1.apresentar())
print(c1.aumentar_salario(50))
print(c1.trocar_setor("TI"))
print(c1.mostrar_dados())

c2 = Funcionario("João", "TI", "Programador", 2000)
print(c2.apresentar())
print(c2.aumentar_salario(50))
print(c2.trocar_setor("Administração"))
print(c2.mostrar_dados())