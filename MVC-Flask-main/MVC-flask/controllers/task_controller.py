from flask import render_template, request, redirect, url_for, Flask, jsonify
from models import db
from models.task import Task
from models.user import User
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)

class TaskController:

    @staticmethod
    @app.route('/tasks/', methods=["GET"])
    def list_tasks():
        
        # TODO buscar todas as tarefas do banco de dados
        tasks = Task.query.all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    @app.route('/tasks/', methods=["POST"])
    def create_task():
        """
        Rota de POST e de GET
        ---
        tags:
          - Tarefas
        description: Cria uma tarefa com título, descrição e user_id
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: body
            name: task
            description: Objeto JSON com os dados da tarefa
            required: true
            schema:
              type: object
              required:
                - title
                - description
                - user_id
              properties:
                title:
                  type: string
                  example: Tarefa de MVC
                description:
                  type: string
                  example: Programa para ler, criar, atualizar e deletar em uma API
                user_id:
                  type: integer
                  example: 3
        responses:
          201:
            description: Retorna a tarefa criada
            schema:
              type: object
              properties:
                title:
                  type: string
                  example: Tarefa de MVC
                description:
                  type: string
                  example: Programa para ler, criar, atualizar e deletar em uma API
                user_id:
                  type: integer
                  example: 3
          400:
            description: Requisição inválida, faltando algum campo
            schema:
              type: object
              properties:
                error:
                  type: string
                  example: "title, description e user_id são obrigatórios"
        """
        data = request.get_json()

        # Validar campos obrigatórios
        if not data or not all(k in data for k in ("title", "description", "user_id")):
            return jsonify({"error": "title, description e user_id são obrigatórios"}), 400

        # Criar e salvar nova tarefa
        new_task = Task(
            title=data['title'],
            description=data['description'],
            user_id=data['user_id']
        )
        db.session.add(new_task)
        db.session.commit()

        # Retornar JSON da tarefa criada
        return jsonify({
            "title": new_task.title,
            "description": new_task.description,
            "user_id": new_task.user_id
        }), 201
    @staticmethod
    @app.route('/tasks/<task_id>', methods=["PUT"])
    def update_task_status(task_id):
        """
        Rota de PUT
---
tags:
  - Tarefas
description: Atualiza uma tarefa existente com título e descrição
consumes:
  - application/json
produces:
  - application/json
parameters:
  - in: body
    name: task
    description: Objeto JSON com os dados da tarefa a ser atualizada
    required: true
    schema:
      type: object
      required:
        - id
        - title
        - description
      properties:
        id:
          type: integer
          example: 3
        title:
          type: string
          example: Tarefa de MVC Atualizada
        description:
          type: string
          example: Programa atualizado para ler, criar, atualizar e deletar em uma api
responses:
  200:
    description: Tarefa atualizada com sucesso
    schema:
      type: object
      properties:
        id:
          type: integer
          example: 3
        title:
          type: string
          example: Tarefa de MVC Atualizada
        description:
          type: string
          example: Programa atualizado para ler, criar, atualizar e deletar em uma api
        user_id:
          type: integer
          example: 3
  400:
    description: Requisição inválida, faltando dados obrigatórios
    schema:
      type: object
      properties:
        error:
          type: string
          example: "id, título e descrição são obrigatórios"
  404:
    description: Tarefa não encontrada
    schema:
      type: object
      properties:
        error:
          type: string
          example: "Tarefa não encontrada"
        """
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
    @app.route('/tasks/<task_id>', methods=["DELETE"])
    def delete_task(task_id):
        """
        Rota de DELETE
---
tags:
  - Tarefas
description: Deleta uma tarefa existente pelo ID
consumes:
  - application/json
produces:
  - application/json
parameters:
  - name: task_id
    in: path
    type: integer
    required: true
    description: ID da tarefa que será deletada
responses:
  200:
    description: Tarefa deletada com sucesso
    schema:
      type: object
      properties:
        message:
          type: string
          example: "Tarefa deletada com sucesso"
  404:
    description: Tarefa não encontrada
    schema:
      type: object
      properties:
        error:
          type: string
          example: "Tarefa não encontrada"
        """
        # TODO buscar a tarefa pelo id
        task = Task.query.get(task_id)
        # TODO: se ela existir, remover do db.session e dar commit
        if task:
            db.session.delete(task)
            db.session.commit()
        else:
            return "Tarefa não encontrada", 404
    
        return redirect(url_for("list_tasks"))