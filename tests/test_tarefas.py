import unittest
import sys
import os

# Adiciona a pasta src ao caminho para conseguirmos importar o código base
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tarefas import GerenciadorTarefas

class TestGerenciadorTarefas(unittest.TestCase):
    def setUp(self):
        # Cria um novo gerenciador 'limpo' antes de cada teste
        self.gerenciador = GerenciadorTarefas()

    def test_adicionar_tarefa_sucesso(self):
        tarefa = self.gerenciador.adicionar_tarefa("Configurar CI", "Criar pipeline no GitHub")
        self.assertEqual(tarefa["titulo"], "Configurar CI")
        self.assertEqual(tarefa["status"], "A Fazer")
        self.assertEqual(len(self.gerenciador.listar_tarefas()), 1)

    def test_adicionar_tarefa_sem_titulo_deve_falhar(self):
        # Testa se o sistema levanta um erro (ValueError) ao enviar um título vazio
        with self.assertRaises(ValueError):
            self.gerenciador.adicionar_tarefa("", "Esta tarefa não tem título")

if __name__ == '__main__':
    unittest.main()
