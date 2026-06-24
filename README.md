# task-manager 📝
Um gerenciador de tarefas via linha de comando (CLI) desenvolvido em Python. Este projeto faz parte do meu aprendizado e desenvolvimento de habilidades de programação, com foco em estruturação de backend, manipulação de arquivos e lógica de programação.
A aplicação permite criar, listar e atualizar tarefas diretamente pelo terminal, armazenando os dados de forma persistente em um arquivo JSON na home do usuário.
🚀 Funcionalidades

Adicionar tarefas via linha de comando
Listar todas as tarefas armazenadas
Atualizar a descrição de uma tarefa por ID
Persistência em JSON usando apenas bibliotecas nativas do Python
Instalação global via pip install . — sem precisar chamar python app.py
Armazenamento automático em ~/.task-manager/tarefas.json, funcionando em qualquer sistema operacional

🛠️ Tecnologias Utilizadas

Python 3.x
Bibliotecas nativas: json, os, argparse

```text
📁 Estrutura do Projeto
taks-manager/
├── app.py                  # Ponto de entrada da CLI
├── models/
│   └── tarefa.py           # Modelo da entidade Tarefa
├── controllers/
│   └── tarefa_controller.py # Regras de negócio e manipulação do JSON
├── pyproject.toml          # Configuração de instalação do pacote
├── .gitignore
└── README.md
```

⚙️ Como Instalar e Usar

1. Clone o repositório:

```bash
git clone https://github.com/rafaelpiva1243/taks-manager.git
```

2. Acesse a pasta do projeto:

```bash
cd taks-manager
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv amb
source amb/bin/activate
```

4. Instale o projeto:

```bash
pip install .
``` 

Use o comando task-manager de qualquer lugar no terminal:

```bash
task-manager --add "Comprar leite"
task-manager --read
task-manager --update 1 "Nova descrição"
```

Os dados são salvos automaticamente em ~/.task-manager/tarefas.json.

📈 Roadmap

 Manipulação de dados em JSON
 Interface via linha de comando com argparse
 Arquitetura com models e controllers (POO)
 Instalação global via pip install .
 Armazenamento portável na home do usuário
 Deletar tarefas
 Alterar status da tarefa (ex: concluído)
 Listar tarefas filtradas por status


Desenvolvido por Rafael Piva Bazani · roadmap.sh · GitHub