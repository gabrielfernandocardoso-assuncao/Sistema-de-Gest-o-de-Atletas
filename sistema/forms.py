# importando a classe do pacote
from flask_wtf import FlaskForm

# importando o tipo de campo e os validators
from wtforms import StringField, EmailField, PasswordField, SubmitField, PasswordField, DateField, FloatField, IntegerField, SelectField

# importando os campos de arquivo
from flask_wtf.file import FileField, FileAllowed

# importando os validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

# importando as tabelas e o db
from sistema import db, bcrypt, app
from sistema.models import Atleta, PlanoTreino, RegistroEvolucao, Exercicio, Usuario  # importar as tabelas do models

# biblioteca usada pra salvar arquivo 
import os

# segurança no bd
from werkzeug.utils import secure_filename

# cadastrar atleta
class CadastroAtletaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    posicao = SelectField('Posição', choices=[('armador', 'Armador'), ('ala', 'Ala'), ('pivo', 'Pivô'), ('ala_armador', 'Ala-Armador'), ('ala_pivo', 'Ala-Pivô')])
    data_nascimento = DateField('Data de nascimento', validators=[DataRequired()])
    peso_atual = FloatField('Peso', validators=[DataRequired()])
    altura = FloatField('Altura', validators=[DataRequired()]) 
    btnsubmit = SubmitField('Registrar')

    # funçao de salvar
    def save(self):
        atleta = Atleta(
            nome = self.nome.data,
            posicao = self.posicao.data,
            data_nascimento = self.data_nascimento.data,
            peso_atual = self.peso_atual.data,
            altura = self.altura.data
        )

        # abrindo uma sessao
        db.session.add(atleta) # passando a variavel criada

        # salvando a sessao
        db.session.commit()


# criar plano de treino
class PlanoTreinoForm(FlaskForm):
    nome_plano = StringField('Nome do plano', validators=[DataRequired()])
    objetivo = StringField('Objetivo', validators=[DataRequired()])
    id_atleta = IntegerField('ID do Dono', validators=[DataRequired()])
    btnsubmit = SubmitField('Registrar')

    def save(self):
        planotreino = PlanoTreino(
            nome_plano = self.nome_plano.data,
            objetivo = self.objetivo.data,
            id_atleta = self.id_atleta.data,
        )

        # abrindo uma sessao
        db.session.add(planotreino) # passando a variavel criada

        # salvando a sessao
        db.session.commit()

# criar registro de exercicio
class ExercicioForm(FlaskForm):
    nome_exercicio = StringField('Nome do Exercicio', validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[('hipertrofia', 'Hipertrofia'), ('forca_maxima', 'Força Máxima'), ('resistencia_muscular', 'Resistência Muscular'), ('funcional', 'Funcional'), ('hiit', 'HIIT'), ('cardio_aerobico', 'Cardio/Aeróbico')])
    btnsubmit = SubmitField('Registrar')

    def save(self):
        exercicio = Exercicio(
            nome_exercicio = self.nome_exercicio.data,
            categoria = self.categoria.data
        )

        # abrindo uma sessao
        db.session.add(exercicio) # passando a variavel criada

        # salvando a sessao
        db.session.commit()

# criar o registro de evolução
class RegistroEvolucaoForm(FlaskForm):
    carga = IntegerField('Carga em KG', validators=[DataRequired()])
    repeticoes = IntegerField('Repetições', validators=[DataRequired()])
    id_atleta = IntegerField('Id do atleta', validators=[DataRequired()])
    id_exercicio = IntegerField('Id do exercicio', validators=[DataRequired()])
    btnsubmit = SubmitField('Registrar')

    def save(self):
        registroevolucao = RegistroEvolucao(
            carga_kg = self.carga.data,
            repeticoes = self.repeticoes.data,
            id_atleta = self.id_atleta.data,
            id_exercicio = self.id_exercicio.data
        )

        # abrindo uma sessao
        db.session.add(registroevolucao) # passando a variavel criada

        # salvando a sessao
        db.session.commit()
