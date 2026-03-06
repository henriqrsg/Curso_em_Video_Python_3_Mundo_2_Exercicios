# PROGRESSÃO ARITMÉTICA MELHORADA #

import os

nome_programa = 'progressão aritmética melhorada'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def pa():
    print('Vamos calcular os termos de uma PA !')
    print()
    quant_termos = int(input('Digite quantos até qual termo da PA você deseja ver: '))
    razao = int(input('Digite a razão da PA: '))
    A1 = int(input('Digite o primeiro termo da PA: '))
    n = 1
    while n <= quant_termos:
        An = A1 + (n-1) * razao
        print('O {}º termo da PA é {}'.format(n, An))
        n += 1

interface()
pa()