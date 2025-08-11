import psycopg2

#Aqui será onde teremos as funcionalidades

def create_User(name):

    #query = "INSERT INTO usuario (id, nome, disciplina) VALUES (%s, %s, %s)"
    #with conn.cursor() as cursor:
        #cursor.execute(query, (id, name, email,))
    #conn.commit()

    print("\n Criado com sucesso!")


def list_User(name):

    print(f"\n {name}")
    