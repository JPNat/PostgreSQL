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

try:

    conn = psycopg2.connect(

        host = hostname,
        dbname = database,
        user = username,
        password = password,
        port = port

    )

    cur = conn.cursor(cursor_factory= psycopg2.extras.DictCursor)


    while True:

        print("\nMenu:")
        print("1 - Inserir Usuario")
        print("2 - Listar Usuario")
        print("3 - Sair")

        opcao = int(input("\nDigite a opção: ")) # Input único e claro

        
        if opcao != 3:

            if opcao == 1:
                
                name = input("Qual o nome do Usuário: ")
                create_User(name)
                #conn.commit()
            
            if opcao == 2:

                name = input("Qual o nome que deseja buscar: ")
                list_User(name)
                #conn.commit()
            
        else:
                
            print("Hasta la vista! \n")
            break

    

    conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    
    if conn is not None:
        conn.close()