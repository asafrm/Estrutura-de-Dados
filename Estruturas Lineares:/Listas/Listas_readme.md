# O que são Listas?

Trabalhando com Estruturas de Dados, utilizamos as listas como uma das ferramentas para implementação dos tipos de dados abstratos. Presente em muitas linguagens de programação, a lista (list) se trata de um mecanismo de coleção de itens, simples e que ao mesmo tempo conta com uma ampla gama de operações que auxiliam na manipulação de dados.

Para um entendimento mais prático do funcionamento de uma lista, podemos fazer uma anaalogia com algo do cotidiano. Relacionando, por exemplo, com uma lista de chamadas de uma instituição:

Imagine uma sala de aula onde o professor possui uma lista com os nomes dos alunos, como Ana, Bruno, Carla, Daniel e Elisa. Essa lista representa uma coleção de itens (os nomes dos alunos), onde cada nome tem uma posição relativa na ordem em que foi registrado. Por exemplo, "Ana" é o primeiro nome, "Bruno" é o segundo, e assim por diante.

Assim como em uma lista de programação, podemos nos referir ao início da lista (o primeiro aluno, "Ana") ou ao final da lista (o último aluno, "Elisa"). Durante a chamada, o professor percorre a lista, verificando a presença de cada aluno. Esse processo é semelhante à interação em uma lista de programação, onde cada elemento é acessado sequencialmente para realizar uma operação, como verificar se o aluno está presente ou ausente.

Outro aspecto importante é que, em uma lista de chamada, cada aluno é único. Não há dois alunos com o mesmo nome na mesma lista, a menos que sejam homônimos, mas mesmo assim são tratados como indivíduos distintos. Da mesma forma, em uma lista desordenada em programação, assumimos que cada elemento é único, a menos que a estrutura permita duplicatas.

Em Python, essa lista de chamada poderia ser representada como:
    lista_chamada = ["Ana", "Bruno", "Carla", "Daniel", "Elisa"]

Assim como na sala de aula, onde o professor pode adicionar novos alunos à lista (por exemplo, "Fernando") ou remover os que já não fazem mais parte da turma (por exemplo, "Daniel"), em programação você pode adicionar ou remover elementos da lista dinamicamente.

# Operações utilizados em Listas

1.  List()
    Usado para criação de uma lista vazia. Não exigindo parâmetros de entrada e retorna uma lista inicializada, porém sem elementos. Em termos práticos, essa função serve para instanciar a estrutura de dados.

2.  add(item)
    Essa operação adiciona um novo elemento à lista. Como parâmetro de entrada, recebe o item a ser adicionado. Essa operação não retorna nenhum valor, mas modifica a lista, incluindo o novo elemento em sua estrutura. Supõe-se que o item ainda não esteja presente na lista.

3.  remove(item)
    Elimina um item específico da lista. Requer o item a ser removido como parâmetro e modifica a lista ao realizar a remoção do elemento. Supõe-se que o item já esteja presente na lista antes da remoção.

4.  search(item)
    Verifica se um item específico está presente na lista. Ela recebe o item como parâmetro e retorna um valor booleano (bool): "True" se o item estiver na lista e "False" se não estiver. Essa função é útil para consultas e validações.

5.  isEmpty():
    Verifica se a lista está vazia. Não requer parâmetros e retorna um valor booleano (bool): "True" se a lista não contiver elementos e "False" caso contrário. Essa função é essencial para evitar operações inválidas, como remover itens de uma lista vazia.

6.  size():
    essa operação retorna o número de itens presentes na lista. Ela não requer parâmetros e retorna um valor inteiro (int), que corresponde à quantidade de elementos armazenados. Essa função é útil para monitorar o estado atual da lista.

7.  append(item):
    A operação append adiciona um novo item ao final da lista, tornando-o o último elemento da coleção. Ela recebe o item como parâmetro e não retorna nenhum valor. Supõe-se que o item ainda não esteja presente na lista.

8.  index(item):
    A operação index retorna a posição (índice) de um item específico na lista. Ela recebe o item como parâmetro e retorna o índice correspondente. Supõe-se que o item já esteja presente na lista.

9.  insert(pos, item):
    A operação insert adiciona um novo item à lista em uma posição específica (pos). Ela recebe o item e a posição como parâmetros e não retorna nenhum valor. Supõe-se que o item ainda não esteja na lista e que a posição indicada seja válida (ou seja, existam itens suficientes para justificar a posição).

10. pop():
    A operação pop remove e retorna o último item da lista. Ela não requer parâmetros e retorna o item removido. Supõe-se que a lista contenha pelo menos um elemento antes da execução.

11. pop(pos):
    A operação pop(pos) remove e retorna o item localizado em uma posição específica (pos) da lista. Ela recebe a posição como parâmetro e retorna o item removido. Supõe-se que o item esteja presente na lista e que a posição seja válida.

# Listas em Python

Utilizando a classe list, criamos uma lista vazia:

    #Criando uma lista vazia para a chamada
    lista_chamada = []

Após a criação da lista, podemos adicionar novos elementos nela, no exemplo a seguir foram utilizados nomes de alunos presentes.

    #Adicionando novos  alunos à lista (operacao append)
    lista_chamada.append("Ana")
    lista_chamada.append("Bruno")
    lista_chamada.append("Carla")
    lista_chamada.append("Daniel")

Para verificarmos se a lista criada está vazia, realizamos o uso da operaçãao "isEmpty". Essa ferramenta é importante para verificarmos se os dados realmente foram inseridos na lista.

    #Verificando se a lista está vazia (operacao isEmpty)
    if not lista_chamada:
        print("A lista de chamada está vazia.")
else:
    print("A lista de chamada não está vazia.")

Para verificar o tamanho da lista fazemos a utilização da operação "size", verificando então quantos elementos estão presentes na lista. Sendo implementada no exemplo para vermos quantos alunos estão presentes.

    #Verificando o tamanho da lista (operacao size)
    print("Número de alunos na lista:", len(lista_chamada))

Para buscarmos um elemento dentro da lista utilizamos uma variável e por meio de "if" "else" realizamos a busca (search). No exemplo usado, a operação serviu para verificar a presença de um aluno:

    #Verificando se um aluno está presente na lista (operacao search)
    aluno_procurado = "Carla"
    if aluno_procurado in lista_chamada:
        print(f"{aluno_procurado} está presente na lista.")
    else:
        print(f"{aluno_procurado} não está presente na lista.")

Para buscarmos a posição que um elemento ocupa dentro da lista podemos utilizar a operação "index". Sendo implementado no seguinte exemplo:

        #Acessando a posição de um aluno na lista (operacao index)
        posicao = lista_chamada.index("Bruno")
        print(f"Bruno está na posição {posicao + 1} da lista.")

Caso o precise inserir um novo elemento na lista, fora do padrão FIFO, podemos fazer uso da operação "insert", que realiza a introdução de um elemento em uma posição expecífica dentro da lista, seguida da posição que deseje alocar o elemento e do então item a ser alocado.

    #Inserindo um novo aluno em uma posição específica (operacao insert)
    lista_chamada.insert(2, "Elisa")  # Inserindo "Elisa" na terceira posição (índice 2)
    print("Lista após inserção de Elisa:", lista_chamada)

Para realizarmos alterações como a remoção de um elemeento presente nafila, podemos fazer uso da ferramenta "remove()" seguido do elemento que se deseja remover , como apresentado no seguinte demonstrativo:

    #Removendo um aluno da lista (operacao remove)
    lista_chamada.remove("Daniel")
    print("Lista após remoção de Daniel:", lista_chamada)

# REFERÊNCIAS:

1.  MILLER, Brad. Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python. Projeto Panda, 2019. Disponível em: https://panda.ime.usp.br/panda/static/pythonds_pt/index.html. Acessado em: 18 mar. 2025.

2.  CARVALHO, Thiago Leite. Estruturas de Dados. São Paulo: Casa do Código, 2024.