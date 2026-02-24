# ESTRUTURAS CONDICIONAIS ANINHADAS #

import os

nome_programa = 'verificando nome'

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa.upper()))
    print(50 * '=')
    print('')

def verificando_nome():
    nome = input('Digite o seu nome: ').lower()
    if nome == 'luiz':
        print('Somos charás! ')
    elif nome in 'joao jose maria paulo ana':
        print('Seu nome é bem comum no Brasil! ')
    else:
        print('Você tem um nome legal! ')


interface()
verificando_nome()