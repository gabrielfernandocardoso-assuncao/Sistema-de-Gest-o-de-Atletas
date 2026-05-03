# importando o aplicativo, db (banco)
from sistema import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request, redirect, flash

# importando as dependencias de login
from flask_login import login_user, logout_user, current_user, login_required

# importando a classe da tabela onde vou salvar
from sistema.models import Atleta, Exercicio, PlanoTreino, RegistroEvolucao, Usuario # alterar de acordo com oque foi criado no models

# importando as classes de formulario
from sistema.forms import CadastroAtletaForm, RegistroEvolucaoForm, ExercicioForm, PlanoTreinoForm  # alterar de acordo com oque foi criado no forms

# criando a homepage ( onde vai ser feito o login )
@app.route('/', methods=['GET', 'POST'])
def Login():

    return render_template('login.html')

# criando o menu ( pagina principal )
@app.route('/menu/', methods=['GET', 'POST'])
def Menu():
    form_atleta = CadastroAtletaForm()
    form_exercicio = ExercicioForm()
    form_planotreino = PlanoTreinoForm()

    # validando o formulario
    if form_atleta.validate_on_submit():
        form_atleta.save()

        return redirect(url_for('Menu'))
    
    # validando o segundo formulario
    if form_exercicio.validate_on_submit():
        form_exercicio.save()

        return redirect(url_for('Menu'))

# validando o terceiro formulario
    if form_planotreino.validate_on_submit():
        form_planotreino.save()

        return redirect(url_for('Menu'))
    
    return render_template('menu.html', titulo_pag="Menu", form_atleta=form_atleta, form_planotreino=form_planotreino, form_exercicio=form_exercicio)

# criando o perfil ( pagina do perfil )
@app.route('/perfil/', methods=['GET', 'POST'])
def Perfil():

    return render_template('perfil.html', titulo_pag="Perfil")

# criando o ver evoluçao
@app.route('/ver-evolucao/', methods=['GET', 'POST'])
def Evolucao():
    form = RegistroEvolucaoForm()

    return render_template('evolucao.html', titulo_pag="Evolução", form = form)