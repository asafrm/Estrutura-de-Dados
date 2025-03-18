# Exemplo de uma lista de chamada em Python

# 1. Criando uma lista vazia para a chamada
lista_chamada = []

# 2. Adicionando novos  alunos à lista (operacao append)
lista_chamada.append("Ana")
lista_chamada.append("Bruno")
lista_chamada.append("Carla")
lista_chamada.append("Daniel")

# Exibindo a lista completa
print("Lista de chamada inicial:", lista_chamada)

# 3. Verificando se a lista está vazia (operacao isEmpty)
if not lista_chamada:
    print("A lista de chamada está vazia.")
else:
    print("A lista de chamada não está vazia.")

# 4. Verificando o tamanho da lista (operacao size)
print("Número de alunos na lista:", len(lista_chamada))

# 5. Verificando se um aluno está presente na lista (operacao search)
aluno_procurado = "Carla"
if aluno_procurado in lista_chamada:
    print(f"{aluno_procurado} está presente na lista.")
else:
    print(f"{aluno_procurado} não está presente na lista.")

# 6. Acessando a posição de um aluno na lista (operacao index)
posicao = lista_chamada.index("Bruno")
print(f"Bruno está na posição {posicao + 1} da lista.")

# 7. Inserindo um novo aluno em uma posição específica (operacao insert)
lista_chamada.insert(2, "Elisa")  # Inserindo "Elisa" na terceira posição (índice 2)
print("Lista após inserção de Elisa:", lista_chamada)

# 8. Removendo um aluno da lista (operacao remove)
lista_chamada.remove("Daniel")
print("Lista após remoção de Daniel:", lista_chamada)

# 9. Removendo o último aluno da lista (operacao pop)
ultimo_aluno = lista_chamada.pop()
print(f"Último aluno removido: {ultimo_aluno}")
print("Lista após remoção do último aluno:", lista_chamada)

# 10. Exibindo a lista final
print("Lista de chamada final:", lista_chamada)