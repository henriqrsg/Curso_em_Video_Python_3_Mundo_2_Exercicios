# CALCULADORA DOIDA #

import os

nome_programa = 'somando numeros ímpares'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')
    print('Vamos somar os números ímpares entre 1 e 500 que são múltiplos de 3')

def calculadora():
    soma = 0
    for i in range(1, 500, 2):
        if i % 3 == 0:
            soma += i
    print(soma)

interface()
calculadora()