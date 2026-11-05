import mysql.connector

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="RPG"
    )

def executar_select(sql):
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
    return colunas, dados

def executar_insert(sql):
    banco = conectar()
    cursor = banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
    banco.close()