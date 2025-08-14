import psycopg2
import psycopg2.extras

#Aqui será onde teremos as funcionalidades

def create_User(cur, conn, rollback, email, nome, telefone, credito, senha, cargo_administrador):

    try:
        insert_usuario = 'INSERT INTO usuario (email, nome, telefone, credito, senha, cargo_administrador) VALUES (%s, %s, %s, %f, %s, %s)'
        #with conn.cursor() as cursor:
        #cursor.execute(query, (id, name, email,))
        #conn.commit()
        insert_value = (email, nome, telefone, credito, senha, cargo_administrador)
        cur.execute(insert_usuario)

        cur.execute('SELECT * FROM usuario')
        for record in cur.fetchall():
            print(record)

        conn.commit()

        print('\n Criado com sucesso!')

    except:
        print('error')

def list_User(cur, nome=''):


    print()

    for item in cur.fetchall():
        print(item)

def commit():
    print() 



def rollback():
    print()
