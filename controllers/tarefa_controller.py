import json
import os
from models.tarefa import Tarefa

class Tarefa_controller(Tarefa):

    def __init__(self):

        diretorio_controller = os.path.dirname(os.path.abspath(__file__))
        diretorio_raiz = os.path.dirname(diretorio_controller)
        
        self.CAMINHO_JSON = os.path.join(diretorio_raiz, "data", "tarefas.json")

    def add_tarefa(self, descricao):
        if descricao:
            dados  = {}

            dados = self.read_json()

            new_task = Tarefa(id=self.id(dados), descricao=descricao)
            
            dados.append(new_task.to_dic())

            if dados:

                with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def read_json(self):
        try:
            with open(self.CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            return dados
        except json.JSONDecodeError as e :
            print(f"erro{e}")
            dados = {}

    def update(self, update, nova_descricao):
        if update:

            dados = {}
            tarefa_encontrada = None

            dados = self.read_json()

            if dados:

                

                for item in dados:    

                    if str(update[0]).strip() == str(item["id"]).strip():
                        tarefa_encontrada = True
                        item["descricao"] = nova_descricao


                if not tarefa_encontrada:
                    print("Nada encontrato")
                else:
                    with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
