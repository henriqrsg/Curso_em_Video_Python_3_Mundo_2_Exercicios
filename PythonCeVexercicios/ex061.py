# PROGRESSÃO ARITMÉTICA #

import os

nome_programa = 'progressão aritmética'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def pa():
    print('Vamos calcular os 10 primeiros termos de uma PA !')
    print()
    razao = int(input('Digite a razão da PA: '))
    A1 = int(input('Digite o primeiro termo da PA: '))
    n = 2
    while n <= 10:
        An = A1 + (n-1) * razao
        print('O A{} é igual a {}'.format(n, An))
        n += 1

interface()
pa()