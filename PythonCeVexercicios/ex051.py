# PROGRESSÃO ARITMÉTICA #

import os

nome_programa = 'progressão aritmética'.upper()

lista_desejo = [
    {'nome': 'An'},
    {'nome': 'Soma'},
    {'nome': 'Razão'}
]

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def deseja():
    for i in range(1, len(lista_desejo) + 1):
        print('[{}] {}'.format(i, lista_desejo[i-1]['nome']))
    print('')
    numero_desejo = int(input('Digite o número do que deseja saber da sua PA: '))
    interface()
    return numero_desejo

def outras_informações(numero_desejo):
    if numero_desejo not in range(1, len(lista_desejo) + 1):
        print('Não existe isto para calcular na PA! ')
    elif numero_desejo == 1:
        n = int(input('Digite o número de n: '))
        a1 = int(input('Digite o valor do A1: '))
        r = int(input('Digite o valor da razão: '))
        an = a1 + ((n-1) * r)
        print('O valor de A{} é igual a {}!'.format(n, an))
    elif numero_desejo == 2:
        n = int(input('Digite o número de n: '))
        a1 = int(input('Digite o valor do A1: '))
        an = int(input('Digite o valor de An'))
        soma = ((a1 + an) * n) / 2
        print('O valor da soma da Pa é igual a {}!'.format(soma))
    elif numero_desejo == 3:
        n = int(input('Digite o número de n: '))
        a1 = int(input('Digite o valor do A1: '))
        an = int(input('Digite o valor de An'))
        r = (an - a1) / (n - 1)
        print('O valor da razão é igual a {}!'.format(r))

interface()
outras_informações(deseja())