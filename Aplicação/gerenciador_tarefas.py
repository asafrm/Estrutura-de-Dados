from collections import deque
 
class ControladorNotas:
    def __init__(self):
        # Inicializa uma fila vazia para armazenar as notas
        self.fila_notas = deque()
 
    def adicionar_nota(self, nota):
        """Adiciona uma nova nota à fila."""
        if isinstance(nota, (int, float)) and 0 <= nota <= 10:  # Valida se a nota é válida (entre 0 e 10)
            self.fila_notas.append(nota)  # Enfileira a nota
            print(f"Nota {nota} adicionada à fila.")
        else:
            print("Erro: A nota deve ser um número entre 0 e 10.")  # Mensagem de erro para notas inválidas
 
    def processar_nota(self):
        """Processa e remove a nota mais antiga da fila."""
        if self.fila_notas:  # Verifica se há notas na fila
            nota_processada = self.fila_notas.popleft()  # Desenfileira a nota
            print(f"Nota {nota_processada} processada.")
        else:
            print("Nenhuma nota para processar.")  # Caso a fila esteja vazia
 
    def listar_notas(self):
        """Exibe todas as notas na fila, da mais antiga para a mais recente."""
        if self.fila_notas:
            print("Notas na fila:")
            for nota in self.fila_notas:
                print(f"- {nota}")
        else:
            print("Nenhuma nota na fila.")  # Caso a fila esteja vazia
 
# Exemplo de uso
if __name__ == "__main__":
    # Criando uma instância do controlador de notas
    meu_controlador = ControladorNotas()
 
    # Adicionando notas à fila
    meu_controlador.adicionar_nota(8.5)
    meu_controlador.adicionar_nota(7.0)
    meu_controlador.adicionar_nota(9.2)
    meu_controlador.adicionar_nota(11)  # Nota inválida (fora do intervalo 0-10)
 
    # Listando todas as notas na fila
    meu_controlador.listar_notas()
 
    # Processando notas (removendo da fila)
    meu_controlador.processar_nota()  # Processa a primeira nota (8.5)
    meu_controlador.processar_nota()  # Processa a próxima nota (7.0)
 
    # Listando novamente para ver as notas restantes
    meu_controlador.listar_notas()
 
    # Tentando processar uma nota quando a fila está vazia
    meu_controlador.processar_nota()
