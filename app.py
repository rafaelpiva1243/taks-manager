import argparse
from datetime import datetime
import json

parser  = argparse.ArgumentParser()

parser.add_argument("--add", help="Adicionar itens")
parser.add_argument("--update")

args = parser.parse_args()


data = datetime.now()


if args.add:
    dados = []

    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
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

    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

if args.update:
    dados = []

    try: 
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except:
        dados = []


