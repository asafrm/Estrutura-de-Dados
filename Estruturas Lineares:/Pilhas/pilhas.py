### Sistema de cadastramento de notas utilizando o sistema de pilhas em Python:

class Nota:              #definição de uma classe
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            raise IndexError("Sem notas encontradas")

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            raise IndexError("Sem notas encontradas")

    def tamanho(self):
        return len(self.itens)

    def __str__(self):
        return str(self.itens)


# Exemplo de uso
nota = Nota()

nota.empilhar(10)
nota.empilhar(9.5)
nota.empilhar(8)
nota.empilhar(5)


print("Notas cadastradas:", nota)  # Saída: Nota: [10, 9.5, 8, 5]

print("Última nota cadastrada:", nota.topo())  # Saída: Topo da pilha: 5

print("Removendo nota:", nota.desempilhar())  # Saída: Removendo nota: 5

print("Notas ainda cadastradas:", nota)  # Saída: Pilha após desempilhar: [10, 9.5, 8]

print("Quantidade de notas cadastradas:", nota.tamanho())  # Saída: Quantidade de notas cadastradas: 3

print("Verificando se não há notas cadastradas:", nota.esta_vazia())  # Saída: False (a pilha não está vazia)