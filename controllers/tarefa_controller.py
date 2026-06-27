import json
import os
from models.tarefa import Tarefa

class Tarefa_controller(Tarefa):

    def __init__(self):

        diretorio_dados = os.path.join(os.path.expanduser("~"), ".task-manager")
        os.makedirs(diretorio_dados, exist_ok=True)
        self.CAMINHO_JSON = os.path.join(diretorio_dados, "tarefas.json")

    def add_tarefa(self, descricao):
        if descricao:
            dados  = {}

            dados = self.read_json()

            new_task = Tarefa(id=self.id(dados), descricao=descricao)
            
            add = dados.append(new_task.to_dic())

            if dados:
                with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                print("Tarefa Adicionada")
                print(new_task.to_dic())
            else:
                print("Erro ao adiconar tarefas")

    def read_json(self):
        existe  = os.path.exists(self.CAMINHO_JSON)
        dados = []

        try:
            if existe:

                with open(self.CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)

                return dados
            else:
                print("Nada encontrado, criando um novo arquivo...")
                with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                    json.dump([], arquivo)
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
                    print("Dados atualizados!")   
            else:
                print("Nenhum dado encontrado")
    
    def read_list(self):
        dados = self.read_json()
        if dados:
            for dado in dados:
                print(dado)
        else:
            print("Sua lista esta vazia")

    def read_id(self, id):
        dados = self.read_json()
        if dados: 
            for data in dados:
                if str(id).strip() == str(data['id']).strip():
                    print(data)
                else:
                    print(f"Nada incontrado como o id: {id}")
        else:
            print("Lista vazia")

    def delete(self, id):
        dados = self.read_json()

        if dados:
            for dado in dados:
                if str(id).strip() == str(dado["id"]).strip():
                    dados.remove(dado)
                    with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def complet(self, complet):
        dados = self.read_json()
        tarefa_encontrada = False

        if dados:

            for dado in dados:
                if str(complet[0]).strip() == str(dado["id"]).strip():
                    tarefa_encontrada = True
                    dado["status"]  = "done"

            if not tarefa_encontrada:
                print("Nada encontrato")
            else:
                with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                print("Dados atualizados!")
                for dado in dados:
                    if str(complet[0]).strip() == str(dado["id"]).strip():
                        print(dado)
        else:
            print("Nenhum dado encontrado")

    def progress(self, progress):
        dados = self.read_json()
        tarefa_encontrada = False

        if dados:

            for dado in dados:
                if str(progress[0]).strip() == str(dado["id"]).strip():
                    tarefa_encontrada = True
                    dado["status"]  = "in progress"

            if not tarefa_encontrada:
                print("Nada encontrato")
            else:
                with open(self.CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                print("Dados atualizados!")
                for dado in dados:
                    if str(progress[0]).strip() == str(dado["id"]).strip():
                        print(dado)
        else:
            print("Nenhum dado encontrado")

    def read_done(self):
        dados = self.read_json()
        if dados: 
            for data in dados:
                if data['status'] == "done":
                    print(data)

        else:
            print("Lista vazia")

    def read_progress(self):
        dados = self.read_json()
        if dados: 
            for data in dados:
                if data['status'] == "in progress":
                    print(data)

        else:
            print("Lista vazia")
