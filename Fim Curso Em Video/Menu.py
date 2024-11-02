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

    print('-=-'*30)
    ret = input(f'{txt}: Digite o numero que deseja acessar \n'.center(90))

    try:
        ret = int(ret)
        if ret >= 0 and ret <= len(tup):
            return ret

    except ValueError:
        ret = ret.upper()
        if ret in tup:
            return ret
