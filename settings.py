#BIBLIOTECAS USADAS

#psycopg2
#psycopg2.extras

import psycopg2
import psycopg2.extras

hostname = 'bancodedadosufs.c6cw1k5vxwqq.us-east-1.rds.amazonaws.com'
database = 'postgres'
username = 'aluno'
password = 'GNUrPQ1TSTcjlr779me2'
port = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(

        host = hostname,
        dbname = database,
        user = username,
        password = password,
        port = port
    )

    cur = conn.cursor(cursor_factory= psycopg2.extras.DictCursor)

except Exception as error:
    print(error)


def read(value):
    try:
        if value == '':
            cur.execute("SELECT * FROM usuario")
            return cur.fetchall()
        else :
            cur.execute("SELECT * FROM usuario WHERE email = %s", (value,))
            return cur.fetchall()
    except Exception as e:
        print(f'Erro: {e}')


def write():
    email = input('Insira um Email')
    nome = input('Insira um nome')
    n = int(input('Quantos telefones deseja inserir'))
    telefones = []
    for x in range(0, n):
        telefone = input()
        telefones.append(telefone)
    credito = int(input('Insira o saldo'))
    senha = input('Insira uma senha')
    tipo_usuario = 1

    valores_usuario = (email, nome, telefones, credito, senha, tipo_usuario)

    try:
        insert_usuario = 'INSERT INTO usuario (email, nome, telefone, credito, senha, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s);'
        cur.execute(insert_usuario, valores_usuario)
        conn.commit();
    except Exception as e:
        conn.rollback()
        return None


def finish():
    if cur is not None:
        cur.close()
    
    if conn is not None:
        conn.close()
