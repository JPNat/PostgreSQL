import settings

def main():
    while True:

        print('\nMenu:')
        print('1 - Inserir Usuario')
        print('2 - Listar Usuarios')
        print('3 - ')
        print('5 - Sair')

        opcao = int(input('\nDigite a opção: ')) # Input único e claro
        

        if opcao != 5:

            if opcao == 1:
                
                nome = input('\nQual o nome do Usuário: \n')
                email = input('\nQual o email do Usuário: \n')
                senha = input('\nQual a senha do Usuário: \n')
                telefone = input('\nQual o telefone do Usuário: \n')
                credito = 0
                cargo_administrador = input('\nEsse usuário é Administrador?: Sim ou Não\n')
            
            if opcao == 2:

                print('\n1 - Para visualizar a tabela completa')
                print('2 - Para buscar por nome')

                opcao = int(input('Selecione a opção de busca:'))

                if opcao == 1:
                    print('Aguarde um momento')

                elif opcao == 2:
                    nome = input('Qual o nome que deseja buscar: ')
            
            if opcao == 3:

                try:
                    print('Aguarde um momento')

                except Exception as error:
                    print(error)

            if opcao == 4:

                print('Tudo certo por enquanto')

                
        print('Hasta la vista! \n')
        break

if __name__ == '__main__':
    main()