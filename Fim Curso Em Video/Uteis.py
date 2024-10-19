import urllib
import urllib.request
import ssl
from time import sleep
from Menu import clear, titulo

def leia_int(valor='Escreva um numero INTEIRO: ' ):
    while True:
        try:
            i = int(input(valor))
            return i
        
        #Tratamento
        except ValueError:
            print(f'\nPor favor, digite um numero Inteiro valido.')

def leia_float(valor='Escreva um numero REAL: ' ):
    while True:
        try:
            f = float(input(valor))
            return f
        
        #Tratamento
        except ValueError:
            print(f'\nPor favor, digite um numero Real valido.')

def leia_str(valor='Escreva um TEXTO: ', str_num=True):
    while True:
        try:
            s = str(input(valor))
            #Tratamento
            if str_num == False:
                try:
                    int(s)
                    print(f'{s}: Por favor, Digite um Texto valido.')
                except:
                    return s
            else:
                return s
        except ValueError:
            print(f'\n{s}: Por favor, Digite um Texto valido.')


def pg(inicio=0, fim=10, razao=1, valor = 0):
    valor += inicio

    #Tratando Razão
    if razao < 0:
        razao *= -1
    elif razao == 0:
        razao = 1

    print('-=-'*30)
    print(f'Contagem de {inicio} até {fim} de {razao} em {razao}')
    sleep(1)

    #Razão Positiva
    if inicio < fim:
        while valor < fim+1:
            print(valor, end='  ', flush=True)
            sleep(0.3)
            valor  += razao
    #Razão Negativa
    else:
        while valor > fim-1:
            print(valor, end='  ', flush=True)
            sleep(0.3)
            valor  -= razao

    print('FIM!')
    print('-=-'*30)
    sleep(2)
    clear()

def check_url(url):
    #Configurando URLLib para não checar Verificado
    ctf = ssl.create_default_context()
    ctf.check_hostname = False
    ctf.verify_mode = ssl.CERT_NONE

    try:
        site = urllib.request.urlopen(url, context=ctf)

    #Tratamento
    except urllib.request.URLError:
        print(f'\nO URL:{url}, está indisponivel no momento.\n')
    except Exception as erro:
        print(f'Algo deu errado.\nERRO>>>{erro.__class__}')
    else:
        print(f'\nO URL:{url}, está disponivel no momento.\n')
    sleep(2)
    clear()

def arquivo_existe(nome):
    try:
        # Arquivo Existe?
        arq = open(nome, 'rt')
        arq.close()
        print('Arquivo Existente.'.center(90))
        return True
    except:
        # Tentando criar arquivo
        try:
            arq = open(nome, 'wt+')
            arq.close()
            print(f'Arquivo {nome} criado com sucesso.'.center(90))
            return False
        
        #Tratamento
        except Exception as erro: 
            print(f'Houve um ERRO na criação do arquivo!\nERRO >>> {erro.__class__}')
    
def ler_arquivo(nome):
    try:
        arq = open(nome, 'rt')
    except Exception as erro:
        print(f'não foi possivel abrir o arquivo {nome}\nERRO>>>{erro.__class__}')
    else:
        clear()
        titulo('Pessoas Cadastradas')
        print(arq.read())
        sleep(5)
        clear()
    arq.close()

def cadastrar_pessoa(arq, nome='desconhecido', idade='-x-'):
    try:
        arquivo = open(arq, 'at')
    except:
        print(f'Falha ao abrir o arquivo')
    else:
        try:
            arquivo.write(f'\n{nome};{idade}')
        except Exception as erro:
            print(f'Algo deu errado na hora de escrever os dados.\nERRO>>> {erro.__class__}')
    print(arq, nome, idade)

    
    