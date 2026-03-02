#Declaração de classe
class Gafanhoto:
    """
Essa classe, cria um gafanhoto, que é uma pessoa que tem nome e idade.
Para criar uma nova pessoa use:
variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = ' ', idade = 0): #Método Construtor
        #Atributos de instância
        self.nome = nome
        self.idade = idade
    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

#Declaração de objetos
g1 = Gafanhoto("Maria", 29)
g1.aniversario()
print(g1)
