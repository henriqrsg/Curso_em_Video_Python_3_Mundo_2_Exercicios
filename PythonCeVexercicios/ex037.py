# CONVERSOR DE BASES BIN OCT HEX #

import os

nome_programa = 'conversor de número inteiro'.upper()

lista_base_conversoes = [
    {'nome': 'binario', 'numero': 1},
    {'nome': 'octal', 'numero': 2},
    {'nome': 'hexadecimal', 'numero': 3},
]

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def escolha_base_convertida():
    print('')
    for n in range(len(lista_base_conversoes)):
        print('[{}] {}'.format(n+1, lista_base_conversoes[n]['nome'].upper()))
    print('')
    numero_base_escolhida = int(input('Digite o número da base que deseja: '))
    print('')
    numero_a_converter = int(input('Digite o número que deseja converter: '))
    print('')
    conversor(numero_base_escolhida, numero_a_converter)

def conversor(numero_base_escolhida, numero_a_converter): 
    if numero_base_escolhida == 1:
        print('O número {} em binario fica {} !'.format(numero_a_converter, bin(numero_a_converter)))
    elif numero_base_escolhida == 2:
        print('O número {} em octal fica {} !'.format(numero_a_converter, oct(numero_a_converter)))
    elif numero_base_escolhida == 3:
        print('O número {} em hexadecimal fica {} !'.format(numero_a_converter, hex(numero_a_converter)))
    else:
        print('Escolha uma base conversora válida! ')
        interface()
        escolha_base_convertida()

interface()
escolha_base_convertida()