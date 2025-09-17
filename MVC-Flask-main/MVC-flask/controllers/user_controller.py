from flask import render_template, request, redirect, url_for
from models.user import User, db

class UserController:
    # A chamada para esse método seria feita diretamente pela classe, sem a necessidade de criar um objeto (uma instância):
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    @staticmethod
    def contact():
        """
        Rota de POST e de GET do usuario
        ---
        tags:
          - Tarefas
        description: Cria e edita um usuario
        consumes:
          - application/json
        produces:
          - application/json
        parameters:
          - in: body
            name: task
            description: Objeto JSON com os dados de um usuario
            required: true
            schema:
              type: object
              required:
                - name
                - email
                - id
              properties:
                name:
                  type: string
                  example: Iago
                email:
                  type: string
                  example: iago.mahiques@aluno.faculdadeimpacta.com.br
                id:
                  type: integer
                  example: 3
        responses:
          201:
            description: Retorna o usuario
            schema:
              type: object
              properties:
                name:
                  type: string
                  example: Iago
                description:
                  type: string
                  example: iago.mahiques@aluno.faculdadeimpacta.com.br
                id:
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
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return render_template('contact.html', error="Usuário com este e-mail já existe", name=name, email=email)

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('contact.html')