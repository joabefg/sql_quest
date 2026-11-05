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

    if ";" not in sql:
        return False, "❌ Todo comando SQL deve terminar com ponto-e-vírgula: ';'."

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

# FASE 02: CONSULTAR O HERÓI
def validar_registro_aventureiro(sql):
    sql = sql.lower()
    
    if "aventureiro" not in sql:
        return False, ("❌ Você precisa consultar na tabela aventureiro.")

    return True, "SQL básico correto!"

def validar_guilda(sql):
    sql = sql.lower()

    if "*" not in sql:
        return False, ("❌ Para esta primeira consulta, use o * para trazer todos os registros.")
        
    if "guilda" not in sql:
        return False, ("❌ Você precisa consultar na tabela guilda.")
    
    return True, "SQL básico correto!"

def validar_guilda_contratante(sql):
    sql = sql.lower()

    if "*" not in sql:
        return False, ("❌ Para esta primeira consulta, use o * para trazer todos os registros.")
        
    if "guilda" not in sql:
        return False, ("❌ Você precisa consultar na tabela guilda.")

    if "where" not in sql:
        return False, ("❌ Você precisa adicionar uma condição usando WHERE.")

    if "=" not in sql:
        return False, ("❌ Você precisa adicionar uma comparação junto com o WHERE, use o '='.")

    if '"contratando"' not in sql:
        return False, ("❌ Você precisa adicionar o estado contratando, entre aspas.")
    
    return True, "SQL básico correto!"

def validar_update(sql):

    sql = sql.lower()

    if "update" not in sql:
        return False, "❌ Você precisa utilizar UPDATE."

    if "set" not in sql:
        return False, "❌ Está faltando SET."

    if "where" not in sql:
        return False, "❌ Está faltando WHERE."

    if "=" not in sql:
            return False, "❌ É necessário ter uma condição usando o WHERE e '='."

    return True, "SQL básico correto!"

def validar_contratacao(sql):
    sql = sql.lower()
    print(sql)

    if "aventureiro" not in sql:
        return False, "❌ Você precisa informar a tabela aventureiro após o UPDATE."

    if "guilda_fk" not in sql:
        return False, "❌ É necessário alterar o campo guilda_fk para inserir o id da guilda. Observe o exemplo do professor ali na esquerda."

    if "guilda_fk=" not in sql and "guilda_fk =" not in sql:
        return False, "❌ guilda_fk precisa ser seguido do id da guilda que você quer participar. exemplo: guilda_fk = 2"

    if 'nome' not in sql and 'id' not in sql:
        return False, '❌ É necessário alterar apenas o seu registro usando a condição WHERE. Pode ser nome = "seu nome" ou id = seu id.'

    return True, "SQL básico correto!"

def validar_delete(sql):

    sql = sql.lower()

    if "delete" not in sql:
        return False, "❌ Você precisa utilizar DELETE."

    if "from" not in sql:
        return False, "❌ Está faltando FROM."

    if "where" not in sql:
        return False, "❌ Está faltando WHERE."

    if "=" not in sql:
        return False, "❌ É necessário ter uma condição usando o WHERE e '='."

    return True, "SQL básico correto!"

def validar_batalha(sql):
    sql = sql.lower()

    if "inimigo" not in sql:
        return False, "❌ Você precisa informar a tabela inimigo após o DELETE."

    if 'nome' not in sql and 'id' not in sql:
        return False, '❌ É necessário alterar apenas o um inimigo usando a condição WHERE. Pode ser nome = "nome do inimigo" ou id = id inimigo.'

    return True, "SQL básico correto!"
    