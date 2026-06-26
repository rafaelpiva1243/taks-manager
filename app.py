import argparse
from datetime import datetime
from models.tarefa import Tarefa
from controllers.tarefa_controller import Tarefa_controller

def main():

    parser  = argparse.ArgumentParser()

    parser.add_argument("--add", help="Adicionar itens")
    parser.add_argument("--update", nargs=2)
    parser.add_argument("--read", help="Lista todas as tarefas", action='store_true')
    parser.add_argument("--delete")
    parser.add_argument("--id", help="Lista por id")
    parser.add_argument("--complet")

    args = parser.parse_args()


    data = datetime.now()

    controler = Tarefa_controller()

    if args.add:
        controler.add_tarefa(args.add)
    elif args.update:
        nova_descricao = " ".join(args.update[1:])
        controler.update(args.update, nova_descricao)
    elif args.read:
        controler.read_list()
    elif args.delete:
        controler.delete(args.delete)
    elif args.id:
        controler.read_id(args.id)
    elif args.complet:
        controler.complet(args.complet)
    else:
        print("Comando não encontrado")


if __name__ == "__main__":
    main()
