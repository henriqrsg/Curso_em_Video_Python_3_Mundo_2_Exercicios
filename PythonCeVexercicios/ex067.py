# NOVA TABUADA #

import os

nome_programa = 'tabuada'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print(f'{nome_programa:^50}')
    print(50 * '=')
    print('')

def tabuada():

    while True:
        interface()
        numero = int(input('Digite o número que deseja saber a tabuada: '))
        print()

        if numero < 0:
            print('PROGRAMA ENCERRADO!')
            break

        for i in range(1, 11):
            print(f'{i} x {numero} = {i * numero}')

        print('')

        input('Digite ENTER para continuar!')

tabuada()