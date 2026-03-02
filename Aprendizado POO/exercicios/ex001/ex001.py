#Declaração de classe
class Gafanhoto:
    def __init__(self): #Método Construtor
        #Atributos de instância
        self.nome = " "
        self.idade = 0
    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

#Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade =29
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Miguel"
g2.idade = 18
print(g2.mensagem())
