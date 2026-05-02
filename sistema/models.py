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
    
# tabela de atletas
class Atleta(db.Model):
    id_atleta = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, nullable = True)
    posicao = db.Column(db.String, nullable = True)
    data_nascimento = db.Column(db.Date, nullable = True)
    peso_atual = db.Column(db.Float, nullable = True)
    altura = db.Column(db.Float, nullable = True)
    user = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    planotreino = db.relationship('PlanoTreino', backref="atleta_dono", cascade="all, delete-orphan", lazy=True)
    dono_registro = db.relationship('RegistroEvolucao', backref="registro_dono", cascade="all, delete-orphan", lazy=True)

# tabela de plano de treino
class PlanoTreino(db.Model):
    id_plano = db.Column(db.Integer, primary_key = True)
    nome_plano = db.Column(db.String, nullable = True)
    objetivo = db.Column(db.String, nullable = True)
    id_atleta = db.Column(db.Integer, db.ForeignKey('atleta.id_atleta'))

# tabela de exercicio 
class Exercicio(db.Model):
    id_exercicio = db.Column(db.Integer, primary_key = True)
    nome_exercicio = db.Column(db.String, nullable = True)
    categoria = db.Column(db.String, nullable = True)
    registro = db.relationship('RegistroEvolucao', backref="exercicio_dono", cascade="all, delete-orphan", lazy=True)

# tabela registro de evolução
class RegistroEvolucao(db.Model):
    id_registro = db.Column(db.Integer, primary_key = True)
    data_treino = db.Column(db.Date, default=datetime.utcnow())
    carga_kg = db.Column(db.Float, default=0)
    repeticoes = db.Column(db.SmallInteger, default=0)
    id_atleta = db.Column(db.Integer, db.ForeignKey('atleta.id_atleta'))
    id_exercicio  = db.Column(db.Integer, db.ForeignKey('exercicio.id_exercicio'))

# apos fazer uma alteração no models, salvar no banco de dados
# flask db migrate
# salvar 
# flask db upgrade
# IMPORTANTE!!! não esquecer, pois dara erro de versionamento.