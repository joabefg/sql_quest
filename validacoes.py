# =========================================
# DESCOBRIR TIPO DE COMANDO
# =========================================

def eh_select(sql):
    return sql.strip().lower().startswith("select")


# =========================================
# COMANDOS BLOQUEADOS
# =========================================

def comando_bloqueado(sql):

    comandos = [
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create"
    ]

    sql = sql.lower()

    for comando in comandos:

        if comando in sql:
            return True, comando

    return False, None


# =========================================
# VALIDAR SELECT
# =========================================

def validar_select(sql):
    sql = sql.strip().lower()

    if not sql.startswith("select"):
        return False, "❌ O comando precisa começar com SELECT."

    if "from" not in sql:
        return False, "❌ Está faltando FROM."

    return True, "SELECT válido."

def validar_cadastro(sql):

    sql = sql.lower()

    if "insert" not in sql:
        return False, "❌ Você precisa utilizar INSERT."

    if "into" not in sql:
        return False, "❌ Está faltando INTO."

    if "values" not in sql:
        return False, "❌ Está faltando VALUES."

    if "(" not in sql:
            return False, "❌ Os nomes e valores devem ser envolvidos por parênteses: (atributo) VALUES ('Texto')."

    return True, "SQL básico correto!"

# FASE 01: REGISTRAR O HERÓI
def validar_registro_aventureiro(sql):

    sql = sql.lower()

    if "aventureiro" not in sql:
        return False, ("❌ Você precisa inserir na tabela aventureiro.")

    if "nome" not in sql:
        return False, ("❌ Você precisa informar o nome.")

    return True, "SQL básico correto!"