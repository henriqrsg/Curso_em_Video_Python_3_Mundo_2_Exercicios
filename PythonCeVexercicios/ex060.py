# FATORIAL #

import os

nome_programa = 'fatorial'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def escolha_numero():
    interface()
    numero = int(input('Digite o número que deseja saber o fatorial: '))
    c = numero - 1
    total = 1
    while c != -1:
        total *= numero - c
        c -= 1
    interface()
    print('O fatorial do numero {} é igual a {}'.format(numero, total))

escolha_numero()