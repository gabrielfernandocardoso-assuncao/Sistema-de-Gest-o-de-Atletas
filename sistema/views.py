# importando o aplicativo, db (banco)
from sistema import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request, redirect, flash

# importando as dependencias de login
from flask_login import login_user, logout_user, current_user, login_required

# importando a classe da tabela onde vou salvar
from sistema.models import Atleta, Exercicio, PlanoTreino, RegistroEvolucao, Usuario # alterar de acordo com oque foi criado no models

# importando as classes de formulario
from sistema.forms import CadastroAtleta, RegistroEvolucao, Exercicio, PlanoTreino  # alterar de acordo com oque foi criado no forms

# criando a homepage ( onde vai ser feito o login )
@app.route('/login/')
def homepage():

    return render_template('homepage')