import argparse
from datetime import datetime
from models.tarefa import Tarefa
from controllers.tarefa_controller import Tarefa_controller

parser  = argparse.ArgumentParser()

parser.add_argument("--add", help="Adicionar itens")
parser.add_argument("--update", nargs=2)

args = parser.parse_args()


data = datetime.now()

controler = Tarefa_controller()

if args.add:
    controler.add_tarefa(args.add)
else:
    nova_descricao = " ".join(args.update[1:])
    controler.update(args.update, nova_descricao)


