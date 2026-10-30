from flask import Flask, render_template, request
from banco import conectar
from validacoes import (
    eh_select,
    validar_select,
    validar_cadastro
)
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registro_aventureiro")
def registro_aventureiro():
    return render_template("registro_aventureiro.html")

@app.route("/registrar_aventureiro", methods=["POST"])
def registrar_aventureiro():
    sql = request.form["sql"].strip()

    # coloca depois
    if not sql:
        return render_template(
            "registro_aventureiro.html",
            mensagem="❌ Digite um comando SQL."
        )
    
    # coloca depois
    if eh_select(sql):
        return executar_select(sql)

    valido, mensagem = validar_cadastro(sql)
    # coloca sem mensagem, depois explica que não tem como o usuário saber o que vai acontecer aí faz o validar cadastro
    # coloca sem o sql, depois explica como é frustrante ficar redigitando aí coloca o sql
    if not valido:
        return render_template(
            "registro_aventureiro.html",
            sql=sql,
            mensagem=mensagem
        )


    return executar_insert(sql)

def executar_select(sql):

    try:
        banco = conectar()
        cursor = banco.cursor()
        cursor.execute(sql)
        dados = cursor.fetchall()
        colunas = [
            coluna[0]
            for coluna in cursor.description
        ]
        cursor.close()
        banco.close()
        return render_template(
            "registro_aventureiro.html",
            sql=sql,
            colunas=colunas,
            dados=dados
        )
    except Exception as erro:
        return render_template(
            "registro_aventureiro.html",
            sql=sql,
            mensagem=f"❌ Erro no SQL: {erro}"
        )

def executar_insert(sql):
    try:
        banco = conectar()
        cursor = banco.cursor()
        cursor.execute(sql)
        banco.commit()
        cursor.close()
        banco.close()
        return render_template(
            "consulta_classe.html",
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


# =========================================
# INICIAR SERVIDOR
# =========================================

app.run(debug=True)