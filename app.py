from flask import Flask, render_template, request
import banco
import validacoes
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registro_aventureiro", methods=["GET"])
def registro_aventureiro():
    return render_template("registro_aventureiro.html")

@app.route("/registrar_aventureiro", methods=["POST"])
def registrar_aventureiro():
    sql = request.form["sql"].strip()

    if not sql:
        return render_template(
            "registro_aventureiro.html",
            mensagem="❌ Digite um comando SQL."
        )
    
    if validacoes.eh_select(sql):
        return executar_select(sql, "registro_aventureiro.html")

    valido, mensagem = validacoes.validar_cadastro(sql)
    if not valido:
        return render_template(
            "registro_aventureiro.html",
            sql=sql,
            mensagem=mensagem
        )
    return executar_insert(sql)

def executar_select(sql, view):

    try:
        colunas, dados = banco.executar_select(sql)
        return render_template(
            view,
            sql=sql,
            colunas=colunas,
            dados=dados,
            mensagem="👍 Sua consulta retornou dados."
        )
    except Exception as erro:
        return render_template(
            view,
            sql=sql,
            mensagem=f"❌ Erro no SQL: {erro}"
        )

def executar_insert(sql):
    try:
        banco.executar_insert(sql)
        return render_template(
            "registro_aventureiro.html",
            mensagem=(
                "Aventureiro cadastrado com sucesso!"
            ),
            sucesso=True
        )
    except Exception as erro:
        return render_template(
            "registro_aventureiro.html",
            sql=sql,
            mensagem=(
                f"❌ O banco recusou o SQL: {erro}"
            )
        )

# GUILDA
@app.route("/guilda")
def consulta_aventureiro():
    return render_template("guilda.html")

@app.route("/consulta_guilda", methods=["POST"])
def consultar_aventureiro():
    sql = request.form["sql"].strip()
    if not sql:
        return render_template(
            "guilda.html",
            mensagem="❌ Digite um comando SQL."
        )
    valido, mensagem = validacoes.validar_select(sql)
    if not valido:
        return render_template(
            "contratacao.html",
            sql=sql,
            mensagem=mensagem
        )
    valido, mensagem = validacoes.validar_guilda(sql)
    if not valido:
        return render_template(
            "guilda.html",
            sql=sql,
            mensagem=mensagem
        )
    try:
        print(sql)
        colunas, dados = banco.executar_select(sql)
        print(colunas)
        print(dados)
        return render_template(
            "guilda.html",
            sql=sql,
            colunas=colunas,
            dados=dados,
            mensagem="👍 Sua consulta retornou dados.",
            sucesso=True
        )
    except Exception as erro:
        return render_template(
            "guilda.html",
            sql=sql,
            mensagem=f"❌ Erro no SQL: {erro}"
        )

# GUILDA CONTRATANTE
@app.route("/guilda_contratante")
def guilda_contratando():
    return render_template("guilda_contratante.html")

@app.route("/consulta_guilda_contratante", methods=["POST"])
def consultar_guilda_contratando():
    sql = request.form["sql"].strip()
    if not sql:
        return render_template(
            "guilda_contratante.html",
            mensagem="❌ Digite um comando SQL."
        )
    valido, mensagem = validacoes.validar_select(sql)
    if not valido:
        return render_template(
            "guilda_contratante.html",
            sql=sql,
            mensagem=mensagem
        )
    valido, mensagem = validacoes.validar_guilda_contratante(sql)
    if not valido:
        return render_template(
            "guilda_contratante.html",
            sql=sql,
            mensagem=mensagem
        )
    try:
        print(sql)
        colunas, dados = banco.executar_select(sql)
        print(colunas)
        print(dados)
        return render_template(
            "guilda_contratante.html",
            sql=sql,
            colunas=colunas,
            dados=dados,
            mensagem="👍 Sua consulta retornou dados.",
            sucesso=True
        )
    except Exception as erro:
        return render_template(
            "guilda_contratante.html",
            sql=sql,
            mensagem=f"❌ Erro no SQL: {erro}"
        )

# CONTRATAÇÃO
@app.route("/contratacao", methods=["GET"])
def contratacao():
    return render_template("contratacao.html")

@app.route("/contratacao", methods=["POST"])
def contratar_guilda():
    sql = request.form["sql"].strip()
    if not sql:
        return render_template(
            "contratacao.html",
            mensagem="❌ Digite um comando SQL."
        )
    
    if validacoes.eh_select(sql):
        return executar_select(sql, "contratacao.html")

    valido, mensagem = validacoes.validar_update(sql)
    if not valido:
        return render_template(
            "contratacao.html",
            sql=sql,
            mensagem=mensagem
        )

    valido, mensagem = validacoes.validar_contratacao(sql)
    if not valido:
        return render_template(
            "contratacao.html",
            sql=sql,
            mensagem=mensagem
        )
    
    try:
        banco.executar_insert(sql)
        return render_template(
            "contratacao.html",
            mensagem=(
                "Parabéns aventureiro! Você foi contratado por uma Guilda."
            ),
            sucesso=True
        )
    except Exception as erro:
        return render_template(
            "contratacao.html",
            sql=sql,
            mensagem=(
                f"❌ O banco recusou o SQL: {erro}"
            )
        )

@app.route("/delete", methods=["GET"])
def view_delete():
    return render_template("boss.html")

@app.route("/delete", methods=["POST"])
def deletar():
    sql = request.form["sql"].strip()

    if not sql:
        return render_template(
            "boss.html",
            mensagem="❌ Digite um comando SQL."
        )
    
    if validacoes.eh_select(sql):
        return executar_select(sql, "boss.html")

    valido, mensagem = validacoes.validar_delete(sql)
    if not valido:
        return render_template(
            "boss.html",
            sql=sql,
            mensagem=mensagem
        )

    valido, mensagem = validacoes.validar_batalha(sql)
    if not valido:
        return render_template(
            "boss.html",
            sql=sql,
            mensagem=mensagem
        )
    
    try:
        banco.executar_insert(sql)
        return render_template(
            "boss.html",
            mensagem=(
                "Inimigo foi eliminado com sucesso! Parabéns bravo herói!"
            ),
            sucesso=True
        )
    except Exception as erro:
        return render_template(
            "boss.html",
            sql=sql,
            mensagem=(
                f"❌ O banco recusou o SQL: {erro}"
            )
        )

# =========================================
# INICIAR SERVIDOR
# =========================================

app.run(debug=True)