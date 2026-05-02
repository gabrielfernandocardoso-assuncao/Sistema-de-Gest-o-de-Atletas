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
@app.route('/')
def Login():

    return render_template('login.html')

# criando o menu ( pagina principal )
@app.route('/menu/')
def Menu():

    return render_template('menu.html', titulo_pag="Menu")

# criando o perfil ( pagina do perfil )
@app.route('/perfil/')
def Perfil():

    return render_template('perfil.html', titulo_pag="Perfil")

# criando o ver evoluçao
@app.route('/ver-evolucao/')
def Evolucao():

    return render_template('evolucao.html', titulo_pag="Evolução")