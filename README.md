# Projetos-flask
criando projetos para treinar flask e demonstrar conhecimento

# criand o sistema de gestao de atletas
    1. criar o ambiente virtual e ativalo
        I. python -m venv venv
    2. preparei o ambiente com tudo que eu precisava pra desenvolver o projeto.
        obs: faltou criar a pasta templates na pasta do app.
    3. instalar as dependencias 
        I. pip install -r requirements.txt
        II. durante o desenvolvimento, se ouver outra instalação salvar com 
            a. pip freeze > requirements.txt
    4. proximo passo é começar o desenvolvimento...

# modelando o banco de dados
    1. no models criar as tabelas(classes)
    2. Explicando cada campo:
        a. db.Column() -> comando dado para criar uma coluna
        b. dentro do db.column, Db.String(#), define o tipo de dado e dentro do parenteses o limite.
            Tipos de dados aceitos:
                Numericos:
                    I. db.Integer: Número inteiro padrão.
                    II. db.SmallInteger: Inteiro pequeno.
                    III. db.BigInteger: Inteiro grande (64 bits).
                    IV. db.Float: Número de ponto flutuante.
                    V. db. Numeric / Decimal: Número de precisão fixa, ideal para valores monetários.
                    VI. db. Boolean: Valor booleano (True / False)
                Strings(textos):
                    I. db.String / VARCHAR: Cadeia de caracteres com tamanho definido.
                    II. db.Text: Cadeia de caracteres de texto longo.
                    III. db.Unicode: String com suporte a Unicode.
                    IV. db.UnicodeText: Texto longo com suporte a Unicode.
                    V. db.CHAR: Caractere de tamanho fixo.
                Data e Hora:
                    I. db.Date: Data (ano, mês, dia).
                    II. db.DateTime: Data e hora.
                    III. db.Time: Hora do dia.
                    IV. db.TIMESTAMP: Carimbo de data/hora.
                Tipos Binários e Grandes Objetos:
                    I. db.Binary / BLOB: Dados binários.
                    II. db.LargeBinary: Objeto binário grande (BLOB).
                Tipos Especiais e Estruturados:
                    I. db.JSON: Suporte para armazenamento de documentos JSON, nativo em bancos como PostgreSQL e MySQL.
                    II. db.ARRAY: Lista de tipos de dados (suportado principalmente pelo PostgreSQL).
                    III. db.Enum: Um valor de uma lista enumerada de opções.
                    IV. db.UUID: Identificador único universal.
    3. atributo primary_key -> define que é uma chave primaria e ja vem com autoincrement
    4. atributo nullable -> define que o dado nao pode estar vazio, "NOT NULL" do sql
    5. .ForeignKey('#.#') -> define chave estrangeira, a propriedade tem que ser o nome da coluna que vai ser referenciada(quase sempre o id da coluna), dentro dos paranteses passar a tabela referenciada, e a coluna que vai acessar, separados por um '.'.
        OBS: toda tabela referenciada pelo FK, tem que ter um atributo com o relationship
    6. .relationship() -> exemplo: 
        a. planotreino = db.relationship('PlanoTreino', backref="atleta_dono", cascade="all, delete-orphan", lazy=True)
            I. 'planotreino' -> nome da propriedade que vai ser acessada. Ex: "atleta.planotreino"
            II. 'PlanoTreino' -> indica em qual classe vai ser conectada. Ex: "PlanoTreino" obs: aqui tem que ser em maiusculo pois esta referindo a table do models
            III. 'backref="atleta_dono" -> atalho para acessar o dono do outro objeto. Ex: "planotreino.atleta_dono"
            III. 'cascade="all"' -> se deletar uma propriedade, deletara as outras conectadas.
            IV. 'delete-orphan' -> se deletar um "link" da propriedade criada "planotreino", o sql define como orfão e o exclui permanentemente
            V. 'lazy=True' -> define o tipo de carregamente, so vai buscar o dando quando for pedido. Economiza memoria.
    7. Criar os formularios no forms -> no forms.py criar a classe dos formularios e importalos no init.py
    8. Criar a homepage, que vai ser a pagina de login no template e definir a rota na view.
    9. Depois de definir o models, ajustar os 2 imports no final da pagina __init__.py.

# criando as paginas(templates)
    1. Na pasta templates, vou criar as paginas principais... (futuramente implemento mais)
    2. criar um base.html pra ser o "pai" das outras pastas "filhos"
    3. Criar o "homepage", por padrao a pagina de login