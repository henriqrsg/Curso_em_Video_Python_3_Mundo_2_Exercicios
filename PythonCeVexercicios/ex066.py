# SOMA DE N NÚMEROS #

import os

nome_programa = 'soma de n números'.upper()

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print('')

def soma():
    interface()
    s = quant = 0
    while True:
        numero = int(input('Digite o número que deseja somar [999 p/ parar]: '))
        if numero == 999:
            break
        s += numero
        quant += 1

    print(f'A soma dos {quant} números digitados foi de {s}')

soma()