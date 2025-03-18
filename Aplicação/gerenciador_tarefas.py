from collections import deque

class GerenciadorTarefas:
    def __init__(self):
        # Inicializa uma fila vazia para armazenar as tarefas
        self.fila_tarefas = deque()

    def adicionar_tarefa(self, tarefa):
        """Adiciona uma nova tarefa à fila."""
        self.fila_tarefas.append(tarefa)  # Enfileira a tarefa
        print(f"Tarefa '{tarefa}' adicionada à fila.")

    def concluir_tarefa(self):
        """Processa e remove a tarefa mais antiga da fila."""
        if self.fila_tarefas:  # Verifica se há tarefas na fila
            tarefa_concluida = self.fila_tarefas.popleft()  # Desenfileira a tarefa
            print(f"Tarefa '{tarefa_concluida}' concluída.")
        else:
            print("Nenhuma tarefa para concluir.")  # Caso a fila esteja vazia

    def listar_tarefas(self):
        """Exibe todas as tarefas na fila, da mais antiga para a mais recente."""
        if self.fila_tarefas:
            print("Tarefas na fila:")
            for tarefa in self.fila_tarefas:
                print(f"- {tarefa}")
        else:
            print("Nenhuma tarefa na fila.")  # Caso a fila esteja vazia

# Exemplo de uso
if __name__ == "__main__":
    # Criando uma instância do gerenciador de tarefas
    meu_gerenciador = GerenciadorTarefas()

    # Adicionando tarefas à fila
    meu_gerenciador.adicionar_tarefa("Comprar mantimentos")
    meu_gerenciador.adicionar_tarefa("Lavar o carro")
    meu_gerenciador.adicionar_tarefa("Estudar para a prova")

    # Listando todas as tarefas na fila
    meu_gerenciador.listar_tarefas()

    # Concluindo tarefas (removendo da fila)
    meu_gerenciador.concluir_tarefa()  # Conclui a primeira tarefa (Comprar mantimentos)
    meu_gerenciador.concluir_tarefa()  # Conclui a próxima tarefa (Lavar o carro)
    meu_gerenciador.concluir_tarefa()  # Conclui a última tarefa (Estudar para a prova)

    # Listando novamente para ver se a fila está vazia
    meu_gerenciador.listar_tarefas()
