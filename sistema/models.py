from sistema import db, login_manager
from datetime import datetime

# Classe usada para informar em qual modelo vai utilizar para fazer login do usuario
from flask_login import UserMixin

# recuperando o usuario
@login_manager.user_loader
def load_user(user_id):

    return Usuario.query.get(user_id)

class Usuario(db.Model, UserMixin): # essa tabela vai ter o login
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String, nullable = True)
    sobrenome = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = True, unique = True)
    senha = db.Column(db.String, nullable = True)
    user = db.relationship('Diagnosticos', backref='user', lazy=True)