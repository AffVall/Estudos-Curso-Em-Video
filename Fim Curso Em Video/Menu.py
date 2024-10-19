import os

def clear():
    os.system('cls')

def titulo(txt='{texto não inserido}'):
    print('-=-'*30)
    print(txt.center(90))
    print('-=-'*30, '\n')

#Criar menu
def op_menu(tup= ('op1', '0p2'), txt={'texto não inserido'}):
    cont = 0
    titulo(f'Escolha: {txt}')

    #Opções
    for v in tup:
        print(f'{cont}-> {v}')
        cont += 1

    while True:
        print('-=-'*30)
        try:
            ret = int(input(f'{txt}: Digite o numero que deseja acessar \n'.center(90)))
            os.system('cls')
            if ret in tup or ret >= 0 and ret <= len(tup):
                return ret
            else:
                print('Esta Aula não existe.'.center(90))
        except:
            print('Digite um valor valido')
