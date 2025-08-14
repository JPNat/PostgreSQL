class ItemLog:

    rollback = ''
    valorNovo = None
    valorAntigo = None

    def __init__(self, id, type, var):
        self.id = id
        self.type = type # start / write / commit / abort / end
        self.var = var
    
    def addRollback (self, command):
        self.rollback = command

    def rollback(self):
        return self.rollback

    def addValores(self, valorNovo, valorAntigo):
        self.valorNovo  = valorNovo
        self.valorAntigo = valorAntigo

import psycopg2
import psycopg2.extras
from functions import create_User, list_User

hostname = 'bancodedadosufs.c6cw1k5vxwqq.us-east-1.rds.amazonaws.com'
database = 'postgres'
username = 'aluno'
password = 'GNUrPQ1TSTcjlr779me2'
port = 5432
conn = None
cur = None

log = list()

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



finally:
    if cur is not None:
        cur.close()
    
    if conn is not None:
        conn.close()
