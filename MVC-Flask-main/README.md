# Gerenciador de Tarefas - MVC com Flask

Este projeto é um gerenciador de tarefas simples desenvolvido em Python utilizando o framework Flask, seguindo o padrão de arquitetura MVC (Model-View-Controller). Ele permite o cadastro de usuários e a criação, listagem, atualização de status e exclusão de tarefas associadas a esses usuários.

## Estrutura do Projeto

```
MVC-FLASK/
│
├── app.py
├── controllers/
│   ├── task_controller.py
│   └── user_controller.py
├── models/
│   ├── __init__.py
│   ├── task.py
│   └── user.py
├── view/
│   ├── config.py
│   └── templates/
│       ├── base.html
│       ├── contact.html
│       ├── create_task.html
│       ├── create_user.html
│       ├── index.html
│       ├── tasks.html
│       └── users.html
├── requirements.txt
└── README.md
```

## Funcionalidades

- Cadastro de usuários
- Cadastro de tarefas vinculadas a usuários
- Listagem de tarefas e usuários
- Atualização do status da tarefa (Pendente/Concluído)
- Exclusão de tarefas

## Como executar

1. **Clone o repositório:**
   ```powershell
   git clone <url-do-repositorio>
   cd MVC-FLASK
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```powershell
   python app.py
   ```

5. **Acesse no navegador:**
   ```
   http://localhost:5002
   ```

## Observações

- O banco de dados utilizado é SQLite e será criado automaticamente como `database.db` na raiz do projeto.
- As configurações estão em `view/config.py`.
- As rotas principais estão definidas em `app.py`.

## Licença

Este projeto é apenas para fins educacionais.
