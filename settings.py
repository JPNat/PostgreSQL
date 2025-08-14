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

rollback = []

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
        print("2 - Listar Usuarios")
        print("3 - Confirmar Mudanças")
        print("4 - Cancelar Mudanças")
        print("5 - Sair")

        opcao = int(input("\nDigite a opção: ")) # Input único e claro
        

        if opcao != 5:

            if opcao == 1:
                
                nome = input("\nQual o nome do Usuário: \n")
                email = input("\nQual o email do Usuário: \n")
                senha = input("\nQual a senha do Usuário: \n")
                telefone = input("\nQual o telefone do Usuário: \n")
                credito = 0
                cargo_administrador = input("\nEsse usuário é Administrador?: Sim ou Não\n")

                create_User(cur, conn, rollback, email, nome, telefone, credito, senha, cargo_administrador)
            
            if opcao == 2:

                print("\n1 - Para visualizar a tabela completa")
                print("2 - Para buscar por nome")

                opcao = int(input("Selecione a opção de busca:"))

                if opcao == 1:
                    list_User(cur)

                elif opcao == 2:
                    nome = input("Qual o nome que deseja buscar: ")
                    list_User(cur, nome)
            
            if opcao == 3:

                try:
                    conn.commit()

                except Exception as error:
                    print(error)

            if opcao == 4:

                rollback.pop()
                print("Item removido de commit")

                
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