### O que são Pilhas?
Uma pilha (stack) se trata de uma estrutura organizada dados, onde elementos podem ser colocados e retirados segindo um princípio.
A estrutura de pilhas é baseada em uma organização cujo princípio é o LIFO (Last In, First Out), por tanto, o último dado que foi inserido na pilha será o primeiro a sair, consequentemente, o primeiro dado inserido, será portanto o último a sair.

### Operações Base de uma Pilha 
Para realizar a estruturação de uma pilha são utilizadas algumas operações, sendo elas:
 
  1.   PUSH: tem a função de empilhar um elemento;
  2. SIZE: retorna o tamanho atual da pilha;
  3. TOP: retorna o valor presente no topo da pilha, sem realizar alteração no elemento;
  4. POP: têm a função de desempilhar elementos na pilha;
  5. EMPTY: verifica se a pilha está vazia.

### Pilhas em Python
Tendo em vista que pilhas se tratam de um tipo de dado abstrado, em python, assim como em outras linguagens de programação orientada a objetos, tratamos esses dados a partir da criação de uma classe.
As operações realizadas com essa pilha são feitas usando métodos dessa classse. Para criar uma pilha, que é uma coleção de elementos, podemos aproveitar a facilidade e a eficiência das estruturas de dados já existentes em Python, como as listas (list).
Uma lista em Python permite armazenar um conjunto de dados de forma ordenada e fornece métodos para manipulá-la. Tomando como exemplo a seguinte lista [1, 2, 3, 4, 5], temos que decidir qual extremidade da lista será o topo da pilha e qual será a base. Após isso, as operações da pilha podem ser feitas usando métodos como append() (para adicionar itenss) e pop(para remover itens).

# Definição de uma classe
class Nota:              
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

Para realizarmos o empilhamento(push) de elementos na pilha, fazemos o seguinte: 

# Exemplo de uso
# Realizando empilhamento (PUSH)
nota = Nota()

nota.empilhar(10)
nota.empilhar(9.5)
nota.empilhar(8)
nota.empilhar(5)

# Método TOP
Para podermos determinar o elemento que está no topo de uma pilha em Python, é necessário implementar manualmente essa operação, uma vez que a linguagem não noss fornece uma função nativa para isso. Podemos então realizar essa operação da seguinte forma:

def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            raise IndexError("Sem notas encontradas")

Executando este código, o valor retornado será 5, que corresponde ao elemento no topo da pilha.

# Método POP

Para remover o elemento do topo da pilha (operação conhecida como pop), utiliza-se o método nota.desempilhar(), por ter sido definido neste exemplo:

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            raise IndexError("Sem notas encontradas")
    
A execução desse comando retorna o valor 5, e a pilha passa a conter apenas os valores [10, 9.5, 8].

# Método SIZE

Para verificar o número de elementos presentes na pilha, utilizamos a função nota.tamanho(). de início, ao realizarmos as operações de empilhamento(push), o tamanho da pilha era 4. Porém, depois da execução de um pop, o tamanho d pilha passou a ser 3.

# Método EMPTY

Para verificar se a pilha está vazia utilizamos a função nota.esta_vazia, como no exemplo:

print("Verificando se não há notas cadastradas:", nota.esta_vazia())  # Saída: False (a pilha não está vazia)

O valor retornado sera False, visto que a pilha possui elemntos cadastrados