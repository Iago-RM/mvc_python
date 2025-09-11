from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)

class TaskController:

    @staticmethod
    def list_tasks():
        # TODO buscar todas as tarefas do banco de dados
        tasks = Task.query.all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        
        if request.method == "POST":
            """
                Rota de post
                    ---
                tags:
                    - Tarefas
                description: Cria uma tarefa com titulo, descricao, e id
                consumes:
                    -application/json
                produces:
                    -application/json
                parameters:
                    -in: body
                    name:task
                    description: Objeto JSON com os dados da tarefa
                    required: true
                    schema:
                        type: object
                        required:
                            -title
                            -email
                        properties:
                            title:
                                type: string
                                example: Tarefa de MVC
                            description:
                                type: string
                                example: Programa para ler, criar, atualizar e deletar em uma api
                responses:
                    201:
                        description: Retorna um novo usuario
                        schema:
                            type: object
                            properties:
                                title:
                                    type: string
                                    example> Tarefa de MVC
                                description:
                                    type: string
                                    example: Programa para ler, criar, atualizar e deletar em uma api
                                user_id: 
                                    type: integer
                                    example: 3
                                            400:
                                                description: Requisição invalida, faltando titulo ou descrição
                                                schema:
                                                    type: object
                                                    properties:
                                                        error:
                                                            type: string
                                                            example: "titulo e descrição são obrigatorios"
                        description:
            """
            # TODO capturar dados do formulário (title, description, user_id)
            title = request.form['title']
            description = request.form['description']
            user_id = request.form['user_id']
            # TODO criar um novo objeto Task com os dados capturados
            new_task = Task(title=title, description=description, user_id=user_id)
            # TODO adicionar no db.session e dar commit
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for("list_tasks"))

        # TODO buscar todos os usuários para exibir no <select> do formulário
        users = User.query.all()
        return render_template("create_task.html", users=users)
    
    @staticmethod
    def update_task_status(task_id):
        # TODO buscar a tarefa pelo id
        task = Task.query.get(task_id)
        # TODO: se existir, alternar status entre "Pendente" e "Concluído" e dar commit na alteração
        if task:
            if task.status == "Pendente":
                task.status = "Concluído"
            else:
                task.status = "Pendente"
            db.session.commit()
        else:
            return "Tarefa não encontrada", 404 

        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        
        # TODO buscar a tarefa pelo id
        task = Task.query.get(task_id)
        # TODO: se ela existir, remover do db.session e dar commit
        if task:
            db.session.delete(task)
            db.session.commit()
        else:
            return "Tarefa não encontrada", 404
    
        return redirect(url_for("list_tasks"))