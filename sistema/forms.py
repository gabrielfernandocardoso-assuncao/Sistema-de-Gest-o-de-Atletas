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

# formulario de cadastro
class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    btnsubmit = SubmitField('Salvar')

    # criando o validador
    def validate_email(self, email):
        if Usuario.query.filter_by(email=email.data).first(): # busca na tabela usuario, na coluna email, o email enviado
            return ValidationError('Usuario já cadastrado com esse Email!!') # resposta do erro

    # criando o save
    def save(self):
        # criptografando a senha
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))

        # criando o usuario
        usuario = Usuario(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        # salvando
        db.session.add(usuario)
        db.session.commit()

        # retorno o usuario para fazer login
        return usuario
    

# formulario de login
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnsubmit = SubmitField('Enviar')

    # função de logar
    def login(self):
        # recupera o usuario
        user = Usuario.query.filter_by(email=self.email.data).first()

        # verificando a senha
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                # retorna o usuario
                return user
            else:
                raise Exception("Senha incorreta!!")
        else:
            return None
        
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

# criar o form de alterar credencias
class AlterarCredenciaisForm(FlaskForm):
    nome = StringField('Novo Nome', validators=[DataRequired()])
    sobrenome = StringField('Novo Sobrenome', validators=[DataRequired()])
    email = EmailField('Novo E-mail', validators=[DataRequired(), Email()])
    senha = StringField('Nova Senha')
    confirmar_senha = StringField('Confirmar a Senha', validators=[EqualTo('senha')])
    foto_perfil = FileField('Foto de Perfil', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg']) ])
    btnsubmit = SubmitField('Alterar')

    def salvar_foto(self, usuario):
        foto = self.foto_perfil.data
        extensao = os.path.splitext(foto.filename)[1]
        nome_arquivo = f"usuario_{usuario.id}{extensao}"
        
        # Caminho absoluto para garantir que o SO encontre a pasta
        caminho_diretorio = os.path.join(app.root_path, 'static', 'foto_perfil')
        
        # Cria a pasta caso ela não exista para evitar erro de "Folder not found"[cite: 17]
        if not os.path.exists(caminho_diretorio):
            os.makedirs(caminho_diretorio)
            
        caminho_completo = os.path.join(caminho_diretorio, nome_arquivo)
        
        # Salva o arquivo e atualiza o banco[cite: 17, 18]
        foto.save(caminho_completo)
        usuario.foto_perfil = nome_arquivo