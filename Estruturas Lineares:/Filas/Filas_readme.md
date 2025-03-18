# O que são Filas?

No nosso cotidiano é muito comum passarmos por situações em que temos de enfrentar filas, seja uma fila de um caixa de supermerrccado, no estacionamento da esola do seu filho, ou até mesmo uma fila de impressão no trabalho. Filas estão presentes no dia a dia dos seres humanos e esse contato nos ajuda a entender com mais failidade a organização das filas em estrutura de dados.
Uma fila se trata de um conjunto de elementos ordenados, possuindo início e fim, este conjunto têm a capacidade de receber e remover elementos. A inclusão de novos elementos ocorre pela extremidade denominada de "fim" (rear), e a remoção ocorre pela outra extremidade, denominada "início" (front). Logo um elemento adicionado em uma fila seguira seu trajeto a partir do rear e terminando no front. 

# Operaações em Filas

As filas são estruturas de dados que seguem o princípio **FIFO** (*First In, First Out*), ou seja, o primeiro elemento a ser inserido é o primeiro a ser removido. Essa característica garante uma ordenação linear e previsível dos elementos. A seguir, são descritas as principais operações associadas a uma fila, conforme padrões acadêmicos:

1. Queue():  
   Responsável por criar uma nova fila vazia. Ela não requer parâmetros de entrada e retorna uma fila inicializada, porém sem elementos. Em termos práticos, essa função serve para instanciar a estrutura de dados.

2. Enqueue(item):  
   A operação "enqueue" adiciona um novo elemento ao final da fila. Como parâmetro de entrada, recebe o item a ser inserido. Essa operação não retorna nenhum valor, mas modifica a fila, incluindo o novo elemento em sua estrutura.

3. Dequeue():  
   A operação "dequeue" remove e retorna o elemento que está no início da fila. Ela não requer parâmetros de entrada, mas altera o estado da fila ao remover o item. O valor retornado corresponde ao elemento que ocupava a primeira posição antes da remoção.

4. isEmpty():  
   Esta operação verifica se a fila está vazia. Ela não necessita de parâmetros e retorna um valor booleano (bool). Caso a fila não contenha elementos, o retorno será "True"; caso contrário, o retorno será "False". Essa função é útil para evitar operações inválidas, como remover elementos de uma fila vazia.

5. Size():  
   A operação "size" retorna o número de elementos presentes na fila. Ela não requer parâmetros e retorna um valor inteiro (int), que corresponde à quantidade de itens armazenados na estrutura. Essa função é essencial para monitorar o estado atual da fila e realizar operações condicionais com base no seu tamanho.

Essas operações formam a base para a manipulação eficiente de filas, garantindo que a estrutura mantenha sua propriedade FIFO e permitindo o gerenciamento adequado dos elementos armazenados.

# Filas em Python

Em python temos a possibilidade de criarmos uma fila seguindo o padrão FIFO, deste modo, elaborando uma fila clássica, ou também podemos elaborar uma dfila de duas cabeças (deque). Analisando os dois formados temos:

# Na prática

Para criar uma fila clássica ou um deque vazio, utiliza-se o seguinte código:

    #Cria uma fila clássica para armazenar as notas dos alunos
    fila_notas = deque()

    #Cria um deque para armazenar as notas dos alunos
    deque_notas = deque()

A fila e deque criados estão vazios, podemos então atribuir valores iniciais para esses conjuntos seguindo seguinte exemplo:

    fila_notas = deque([6, 4.5, 9])
    deque_notas = deque([6, 4.5, 9])

E para que seja inserido elementos nesses conjuntos, utilizamos métodos como:

    #Adiciona notas à fila (enqueue)
    fila_notas.append(7.5)  # Nota do aluno 1
    fila_notas.append(8.0)  # Nota do aluno 2
    fila_notas.append(5.5)  # Nota do aluno 3

Para remover algum elemento do conjunto, utilizamos o seguinte método:

    nota = fila_notas.popleft()  # Remove a nota mais antiga (dequeue)

Para verificar se a fila está vazia, utilizamos:

    len(fila_notas) == 0:  # Verifica se o deque está vazio

Se desejarmos verificar o tamanho da fila, usamos o seguinte método:

    len(fila_notas) #Retorna a quantidade de elementos presentes na fila

Também temos a possibilidade de verificar quantas vezes um elemento foi repetido dentro de uma fila, seguindo o método:

    fila_notas.count(7.5) #Retorna o número de vezes que a nota foi repetida

Como diferencial, um deque conto com método que possibilita a inserção de um elemento no ínicio da fila e não apenas no fim:    

    # Adiciona uma nota prioritária no início do deque
    deque_notas.appendleft(8.5)  # Nota prioritária do aluno 5