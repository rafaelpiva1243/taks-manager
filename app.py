import argparse
from datetime import datetime
import json

parser  = argparse.ArgumentParser()

parser.add_argument("--add")

args = parser.parse_args()


data = datetime.now()

tarefas = {
    "id": "",
    "descricao": args.add,
    "status": "pendente",
    "createdAt": f"{data}",
    "updatedAt": f"{data}"
},


if args.add:
    dados = []

    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except json.JSONDecodeError as e :
        print(f"erro{e}")

    dados.append(tarefas)

    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)



