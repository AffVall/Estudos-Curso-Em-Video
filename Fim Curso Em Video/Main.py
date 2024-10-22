import Uteis
from Menu import *

ex = ('Fim', 98, 113, 114, 115)
titulo('Benvindo ao Arquivo de aulas Curso Em Video')
while True:

    escolha = op_menu(ex, 'Aula')

    # Saindo do programa
    if escolha == 0:
        titulo('Codigo encerrado.')
        break

    #PG
    elif escolha == 98 or escolha == 1:
        #Demonstração
        Uteis.pg()
        Uteis.pg(5, -5, 2)

        #Inserindo Valores
        i = int(input('Digite o INICIO de sua PG: '))
        f = int(input('Digite o FIM da sua PG: '))
        r = int(input('Digite a RAZÃO da sua PG: '))
        Uteis.pg(i, f, r)

    #Divisão entre Valor Inteiro e Real
    elif escolha == 113 or escolha == 2:
        #Inserindo valores
        i = Uteis.leia_int()
        r = Uteis.leia_float()

        #Demonstrando Valores
        clear()
        print(f'O valor INTEIRO é {i} e o valor REAL é {r}')
        Uteis.sleep(3)
        clear()

    #Verificando se URL está ativo
    elif escolha == 114 or escolha == 3:
        Uteis.check_url('https://www.pudim.com.br/')
        while True:
            try:
                url = input('Digite o URL que deseja verificar: ')
                Uteis.check_url(url)

            #Tratamento
            except ValueError:
                if url == '':
                    clear()
                    break
                print(f'Não é um URL valido, digite um URL existente.\n')
            except Exception as erro:
                print(f'ERRO>>> {erro.__cause__}')
            
    #Cadastro de pessoas
    elif escolha == 115 or escolha == 4:
        arquivo = 'cadastro.txt'
        opcoes = ('Sair' ,'Ver pessoas cadastradas', 'Cadastrar nova pessoa')

        titulo('Menu de Cadastros')
        Uteis.arquivo_existe(arquivo)
        while True:
            menu = op_menu(opcoes, 'Cadastro')

            #Sair
            if menu == 0 or menu == 'Sair':
                break
            
            #Ler Arquivo
            if menu == 1 or menu == 'Ver pessoas cadastradas':
                Uteis.ler_arquivo(arquivo)
            
            #Escrever no arquivo
            if menu == 2 or menu == 'Cadastrar nova pessoa':
                clear()
                titulo('Novo Cadastro')
                nome = Uteis.leia_str('Escreva o NOME da pessoa cadastrada: ', False)
                idade = Uteis.leia_int('Escreva a IDADE da pessoa cadastrada: ')
                Uteis.cadastrar_pessoa(arquivo, nome, idade)
            
