import argparse
from datetime import datetime
import json
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_JSON = os.path.join(DIRETORIO_ATUAL, "data", "tarefas.json")

parser  = argparse.ArgumentParser()

parser.add_argument("--add", help="Adicionar itens")
parser.add_argument("--update", nargs=2)

args = parser.parse_args()


data = datetime.now()


if args.add:
    dados = []

    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except json.JSONDecodeError as e :
        print(f"erro{e}")

    
    if len(dados) == 0:
        novo_id = 1
    else:
        novo_id = dados[-1]["id"] + 1

    tarefas = {
        "id": novo_id,
        "descricao": args.add,
        "status": "pendente",
        "createdAt": f"{data}",
        "updatedAt": f"{data}"
    }

    dados.append(tarefas)

    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

if args.update:
    dados = {}
    tarefa_encontrada = None

    try: 
        with open("./data/tarefas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except:
        dados = {}

    nova_descricao = " ".join(args.update[1:])

    for item in dados:    

        if str(args.update[0]).strip() == str(item["id"]).strip():
            tarefa_encontrada = True
            item["descricao"] = nova_descricao


    if not tarefa_encontrada:
        print("Nada encontrato")
    else:
        with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            


