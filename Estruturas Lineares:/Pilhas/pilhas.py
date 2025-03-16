class Pilha:
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
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.itens)

    def __str__(self):
        return str(self.itens)


# Exemplo de uso
pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.empilhar(40)
pilha.empilhar(50)


print("Pilha:", pilha)  # Saída: Pilha: [10, 20, 30, 40, 50]

print("Topo da pilha:", pilha.topo())  # Saída: Topo da pilha: 50

print("Desempilhando:", pilha.desempilhar())  # Saída: Desempilhando: 50

print("Pilha após desempilhar:", pilha)  # Saída: Pilha após desempilhar: [10, 20, 30, 40]

print("Tamanho da pilha:", pilha.tamanho())  # Saída: Tamanho da pilha: 4