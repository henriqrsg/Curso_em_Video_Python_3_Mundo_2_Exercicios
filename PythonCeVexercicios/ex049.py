# TABUADA #

import os

nome_programa = 'tabuada'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def escolhendo_numero():
    numero_escolhido = int(input('Digite o número que deseja saber a tabuada: '))
    print('')
    return numero_escolhido

def tabuada(numero_escolhido):
    for i in range (1, 11):
        print('{} x {} = {}'.format(i, numero_escolhido, numero_escolhido * i))

interface()
tabuada(escolhendo_numero())