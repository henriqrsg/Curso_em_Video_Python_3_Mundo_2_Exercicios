# VERIFICADOR DE NÚMERO PRIMO #

import os

nome_programa = 'verificador de número primo'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def pegando_numero():
    numero = int(input('Digite o número que deseja verificar se é um número primo: '))
    return numero

def verificador(numero):
    if numero == 1:
        print('O número 1 não é primo! ')
    else: 
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                print('O número {} não é primo'.format(numero))
                primo = False
                break
        if primo == True:
            print('O número {} é primo'.format(numero))

interface()
verificador(pegando_numero())