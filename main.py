from settings import read as r
from settings import write as w
from settings import finish as f

def main():
    while True:

        print('\nMenu:')
        print('1 - Inserir Usuario')
        print('2 - Listar Usuarios')
        print('3 - Fechar')
        print('5 - Sair')

        opcao = int(input('\nDigite a opção: ')) # Input único e claro
        
        print('Transação Iniciada')

        if opcao != 5:

            if opcao == 1:

                w()
                
            if opcao == 2:

                print('Insira um nome para buscar na tabela ou aperte enter para buscar todos os itens')
                
                email = input()

                r(email)
            
            if opcao == 3:

                f()
                print('Hasta la vista! \n')
                break
        
        print('Transação Finalizada')

if __name__ == '__main__':
    main()
