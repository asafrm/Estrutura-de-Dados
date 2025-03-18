### Exemplo 1: Fila Clássica (FIFO)
### Neste exemplo, uma fila clássica é utilizada para processar as notas dos alunos na ordem em que foram inseridas. A ideia é calcular a média das notas e verificar se o aluno foi aprovado (média ≥ 6) ou reprovado.

from collections import deque

# Cria uma fila clássica para armazenar as notas dos alunos
fila_notas = deque()

# Adiciona notas à fila (enqueue)
fila_notas.append(7.5)  # Nota do aluno 1
fila_notas.append(8.0)  # Nota do aluno 2
fila_notas.append(5.5)  # Nota do aluno 3
fila_notas.append(7.5)  # Nota do aluno 4


# Processa as notas na ordem FIFO
while not len(fila_notas) == 0:
    nota = fila_notas.popleft()  # Remove a nota mais antiga (dequeue)
    if nota >= 6:
        print(f"Aluno com nota {nota}: Aprovado")
    else:
        print(f"Aluno com nota {nota}: Reprovado")

# Verifica se a fila está vazia após o processamento
    if len(fila_notas) == 0:  # Verifica se o deque está vazio
        print("Todas as notas foram processadas.")

### Exemplo 2: Deque (Fila de Duas Extremidades)
### Neste exemplo, um deque é utilizado para gerenciar as notas dos alunos, permitindo operações tanto no início quanto no final da fila. Aqui, o deque é usado para adicionar novas notas no final e processar as notas mais recentes primeiro (LIFO - Last In, First Out).

from collections import deque

# Cria um deque para armazenar as notas dos alunos
deque_notas = deque()

# Adiciona notas ao deque (enqueue no final)
deque_notas.append(6.0)  # Nota do aluno 1
deque_notas.append(4.5)  # Nota do aluno 2
deque_notas.append(9.0)  # Nota do aluno 3
deque_notas.append(9.0)  # Nota do aluno 4

# Adiciona uma nota prioritária no início do deque
deque_notas.appendleft(8.5)  # Nota prioritária do aluno 5

# Processa as notas mais recentes primeiro (LIFO)
while len(deque_notas) > 0:
    nota = deque_notas.pop()  # Remove a nota mais recente (do final)
    if nota >= 6:
        print(f"Aluno com nota {nota}: Aprovado")
    else:
        print(f"Aluno com nota {nota}: Reprovado")

# Verifica se o deque está vazio após o processamento
if len(deque_notas) == 0:
    print("Todas as notas foram processadas.")  