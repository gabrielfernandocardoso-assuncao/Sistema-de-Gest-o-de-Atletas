# importando a classe do pacote
from flask_wtf import FlaskForm

# importando o tipo de campo e os validators
from wtforms import StringField, EmailField, PasswordField, SubmitField, PasswordField, DateField, FloatField, IntegerField

# importando os campos de arquivo
from flask_wtf.file import FileField, FileAllowed

# importando os validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

# importando as tabelas e o db
from sistema import db, bcrypt, app
from sistema.models import Atleta # importar as tabelas do models

# biblioteca usada pra salvar arquivo 
import os

# segurança no bd
from werkzeug.utils import secure_filename

# cadastrar atleta
class CadastroAtleta(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    posicao = StringField('Posição', validators=[DataRequired()])
    data_nascimento = DateField('Data de nascimento', validators=[DataRequired()])
    peso = FloatField('Peso', validators=[DataRequired()])
    altura = FloatField('Altura', validators=[DataRequired()]) 

# criar plano de treino
class PlanoTreino(FlaskForm):
    nome_plano = StringField('Nome do plano', validators=[DataRequired()])
    objetivo = StringField('Objetivo', validators=[DataRequired()])
    id_atleta = IntegerField('ID do Dono', validators=[DataRequired()])

# criar registro de exercicio
class Exercicio(FlaskForm):
    nome_exercicio = StringField('Nome do Exercicio', validators=[DataRequired()])
    categoria = StringField('Categoria', validators=[DataRequired()])
    
# criar o registro de evolução
class RegistroEvolucao(FlaskForm):
    carga = IntegerField('Carga em KG', validators=[DataRequired()])
    repeticoes = IntegerField('Repetições', validators=[DataRequired()])
    id_atleta = IntegerField('Id do atleta', validators=[DataRequired()])
    id_exercicio = IntegerField('Id do exercicio', validators=[DataRequired()])

