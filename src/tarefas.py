class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, titulo, descricao):
        if not titulo:
            raise ValueError("O título da tarefa é obrigatório.")
        tarefa = {
            "id": self.proximo_id,
            "titulo": titulo,
            "descricao": descricao,
            "status": "A Fazer"
        }
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def atualizar_status(self, id_tarefa, novo_status):
        for t in self.tarefas:
            if t["id"] == id_tarefa:
                t["status"] = novo_status
                return t
        return None

    def remover_tarefa(self, id_tarefa):
        tarefas_iniciais = len(self.tarefas)
        self.tarefas = [t for t in self.tarefas if t["id"] != id_tarefa]
        return len(self.tarefas) < tarefas_iniciais
