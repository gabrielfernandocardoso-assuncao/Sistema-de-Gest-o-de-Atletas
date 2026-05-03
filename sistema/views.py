# importando o aplicativo, db (banco)
from sistema import app, db

# importando a função render_template, url_for
from flask import render_template, url_for, request, redirect, flash

# importando as dependencias de login
from flask_login import login_user, logout_user, current_user, login_required

# importando a classe da tabela onde vou salvar
from sistema.models import Atleta, Exercicio, PlanoTreino, RegistroEvolucao, Usuario # alterar de acordo com oque foi criado no models

# importando as classes de formulario
from sistema.forms import CadastroAtletaForm, RegistroEvolucaoForm, ExercicioForm, PlanoTreinoForm, CadastroForm, LoginForm, AlterarCredenciaisForm  # alterar de acordo com oque foi criado no forms

# importando o bcrypt
from sistema import bcrypt

# criando a homepage ( onde vai ser feito o login )
@app.route('/', methods=['GET', 'POST'])
def Login():
    # criando o bloco de login
    form_cadastro = CadastroForm() # instanciando o formulario de cadastro
    form_login = LoginForm() # instanciando o formulario de login

    # verificando login
    if form_login.validate_on_submit():
        user = form_login.login()
        if user:
            login_user(user, remember=True)
            return redirect(url_for('Menu'))
        else:
            flash('E-mail ou Senha incorretos!', 'danger')

    # verificando cadastro
    if form_cadastro.validate_on_submit():
        # se estiver aqui, ja verificou se o email não é repetido
        user = form_cadastro.save()
        # se user nao for vazio
        if user:
            login_user(user, remember=True)
            return redirect(url_for('Menu'))
        else:
            flash('Erro ao criar usuario. Tente Novamente.', 'danger')

    return render_template('login.html', form_cadastro=form_cadastro, form_login=form_login)

# criando o logout(sair)
@app.route('/sair/')
def Logout():
    logout_user()

    return redirect(url_for('Login'))
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
@login_required # garantindo que so tera um usuario logado
def Perfil():
    form = AlterarCredenciaisForm()

    # verificando se o metodo é post
    if form.validate_on_submit():
        current_user.nome = form.nome.data
        current_user.sobrenome = form.sobrenome.data
        current_user.email = form.email.data

        # chamando a função de salvar foto
        if form.foto_perfil.data:
            form.salvar_foto(current_user)

        # criptografando a senha
        if form.senha.data:
            current_user.senha = bcrypt.generate_password_hash(form.senha.data.encode('utf-8'))

        # salvando os dados no db
        db.session.commit()

        flash('Perfil atualizado com sucesso!', 'sucesses')

    # preenche os dados com os ja existente
    elif request.method == 'GET':
        form.nome.data = current_user.nome
        form.sobrenome.data = current_user.sobrenome
        form.email.data = current_user.email

    if form.errors:
        print(form.errors)
        
    return render_template('perfil.html', titulo_pag="Perfil", form=form)

# criando o ver evoluçao
@app.route('/ver-evolucao/', methods=['GET', 'POST'])
def Evolucao():
    form = RegistroEvolucaoForm()
    
    # se o request for post
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            flash('Salvo com sucesso!', 'success')

    # se o request for get
    busca = request.args.get('busca', '')

    # juntando as tabelas para permirtir pesquisas mais complexas
    query = RegistroEvolucao.query.join(Atleta)


    if busca != "":
        # filtrar pelo nome do atleta
        query = query.filter(Atleta.nome.contains(busca))

    
    # buscando os registro
    dados = query.order_by(RegistroEvolucao.id_registro).all()
    
    context = { 'dados' : dados }
    return render_template('evolucao.html', titulo_pag="Evolução", form = form, context=context, busca=busca)