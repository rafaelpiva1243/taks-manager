from datetime import datetime

class Tarefa():
    
    def __init__(self, id, descricao, status="pendente", createdAt=None, updatedAt=None):
        self.id = id
        self.descricao = descricao
        self.status = status

        date = str(datetime.now())
        self.createdAt = date
        self.updatedAt = date

    def id(self, dados):

        if len(dados) == 0:
            novo_id = 1
            
        else:
            novo_id = dados[-1]["id"] + 1
    
        return novo_id

    def atualizar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
        self.updatedAt = str(datetime.datetime.now())

    def concluir(self):
        self.status = "concluído"
        self.updatedAt = str(datetime.datetime.now())

    def to_dic(self):
        return {
            "id": self.id,
            "description": self.descricao,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }