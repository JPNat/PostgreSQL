import psycopg2
import psycopg2.extras

#Aqui será onde teremos as funcionalidades

def create_User(cur, roolback):

    try:
        insert_usuario = 'INSERT INTO usuario (email, nome, telefone, credito, senha, cargo_administrador) VALUES (%s, %s, %s, %f, %s, %s)'
        #with conn.cursor() as cursor:
        #cursor.execute(query, (id, name, email,))
        #conn.commit()
        insert_value = ('fulaninho@gmail.com', 'Fulaninho Silva Santos', '79 9.1234-4321', 0.00, 'Senha Segura', 'Falso')
        cur.execute(insert_usuario)

        cur.execute('SELECT * FROM usuario')
        for record in cur.fetchall():
            print(record)
            
        conn.commit()

        print('\n Criado com sucesso!')

    except:
        print('error')

def list_User(cur, nome=''):

    if nome == '':
        cur.execute(f'SELECT * FROM usuario')
    else:
        cur.execute(f'SELECT * FROM usuario WHERE nome = \'{nome}\'')

    print()

    for item in cur.fetchall():
        print(item)

def commit():
    print() 



def rollback():
    print()