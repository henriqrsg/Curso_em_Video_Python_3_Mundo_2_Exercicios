# VERIFICADOR DE ALISTAMENTO #

import os

nome_programa = 'verificador de alistamento'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def verificando_idade():
    idade = int(input('Digite a sua idade: '))
    print()
    if idade < 18:
        anos_p_alistar = 18 - idade
        print('Você ainda é muito novo! Não está na hora de alistar! Ainda faltam {} ano/s para você se alistar!'.format(anos_p_alistar))
    elif idade == 18:
        print('Está na hora de você se alistar!')
    else: 
        anos_p_alistar = idade - 18
        print('Já passou da hora de você se alistar! Era para você ter se alistado a {} ano/s!'.format(anos_p_alistar))

interface()
verificando_idade()