from models import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Task(db.Model):
    __tablename__ = "tasks"
    # TODO: Define os campos e o relacionamento da tabela Task
    # - id: chave primária da tarefa
    id = db.Column(db.Integer, primary_key=True)
    # - title: título da tarefa (obrigatório)
    title = db.Column(db.String(100), nullable=False)
    # - description: descrição detalhada da tarefa (obrigatório)
    description = db.Column(db.String(250), nullable=False)
    # - user_id: chave estrangeira que conecta a tarefa a um usuário (não nulo)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # - status: indica o estado da tarefa, padrão "Pendente"
    status = db.Column(db.String(10), default="Pendente")
    # - user: relacionamento com a classe User, usando back_populates="tasks" para criar o vínculo bidirecional
    user = db.relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"