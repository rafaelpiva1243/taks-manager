# taks-manager
 
# CLI Task Manager 📝

Um gerenciador de tarefas via linha de comando (CLI) desenvolvido em Python. Este projeto prático faz parte do meu aprendizado e desenvolvimento das minhas habilidades de programação, com foco em estruturação de backend, manipulação de arquivos e lógica de programação.

A aplicação permite que você crie, atualize e gerencie suas tarefas diárias diretamente pelo terminal do sistema operacional, armazenando os dados de forma persistente em um arquivo JSON.

## 🚀 Funcionalidades

* **Manipulação de Dados em JSON:** Leitura e escrita de dados utilizando a biblioteca nativa do Python.
* **Interface via Linha de Comando:** Utilização do `argparse` para capturar argumentos e executar ações diretamente pelo terminal.
* **Atualização de Tarefas:** Busca de tarefas por ID e alteração de descrições em tempo real.
* **Organização de Diretórios:** Separação lógica entre os scripts executáveis (`core`) e o armazenamento de dados (`data`).

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Bibliotecas nativas:** `json`, `os`, `argparse`

## 📁 Estrutura do Projeto

O projeto segue uma organização limpa, separando a regra de negócio do banco de dados:

```text
taks-manager/
├── app.py               # Script principal responsável por receber os comandos
├── data/
│   └── tarefas.json     # Arquivo de armazenamento de dados (simulando um banco de dados)
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Documentação do projeto

⚙️ Como Executar
1. Clone este repositório para a sua máquina:
```
git clone [https://github.com/rafaelpiva1243/taks-manager.git](https://github.com/rafaelpiva1243/taks-manager.git)
```

2.Acesse a pasta do projeto:

```
cd taks-manager
```

3. Execute o script passando os argumentos desejados. Exemplo para atualizar uma tarefa:

```
python app.py --update 1 "Nova descrição da tarefa"
```

📈 Próximos Passos (Roadmap)
[x] Implementar atualização de descrição de tarefas.

[x] Isolar o arquivo JSON em um diretório data/.

[ ] Refatorar a arquitetura utilizando Programação Orientada a Objetos (POO), separando em models e controllers.

[ ] Adicionar funcionalidade para deletar tarefas.

[ ] Adicionar funcionalidade para alterar o status da tarefa (ex: "concluído").

Desenvolvido por Rafael Piva Bazani com https://roadmap.sh/projects/task-tracker. 


