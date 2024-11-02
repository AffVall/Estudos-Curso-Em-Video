import Uteis
from Menu import *

EX = ('FIM', 'PG', 'DIVISAO', 'URL', 'CADASTRO', 'CPF')
titulo('Benvindo ao Arquivo de exercicios :D')
while True:
    escolha = op_menu(EX, 'Aula')
    # Saindo do programa
    if escolha == EX[0] or escolha == 0 :
        titulo('Codigo encerrado.')
        break

#
    #PG
    elif escolha == EX[1] or escolha == 1:
        clear()
        #Demonstração
        Uteis.pg()
        Uteis.pg(5, -5, 2)

        #Inserindo Valores
        i = int(input('Digite o INICIO de sua PG: '))
        f = int(input('Digite o FIM da sua PG: '))
        r = int(input('Digite a RAZÃO da sua PG: '))
        Uteis.pg(i, f, r)
        clear()

    #Divisão entre Valor Inteiro e Real
    elif escolha == EX[2] or escolha == 2:
        #Inserindo valores
        i = Uteis.leia_int()
        r = Uteis.leia_float()

        try: 
            d = i/r
            clear()
            print(f'O valor INTEIRO é {i} e o valor REAL é {r} e a divisão entre eles é {d}')
            Uteis.sleep(3)
            clear()
        except ZeroDivisionError: 
            print('Não é possivel fazer divisão por ZERO.')

        #Demonstrando Valores

    #Verificando se URL está ativo
    elif escolha == EX[3] or escolha == 3:
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
    elif escolha == EX[4] or escolha == 4:
        arquivo = 'cadastro.txt'
        EX = ('Sair' ,'Ver pessoas cadastradas', 'Cadastrar nova pessoa')

        clear()
        titulo('Menu de Cadastros')
        Uteis.arquivo_existe(arquivo)
        while True:
            menu = op_menu(EX, 'Cadastro')

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
            
#Curso {Python 3 Completo}
    #Gerar CPF
    elif escolha == EX[5] or escolha == 5:
        real_cpf = Uteis.verif_cpf()

    





    else:
        print('Esta aula não existe'.center(90))
