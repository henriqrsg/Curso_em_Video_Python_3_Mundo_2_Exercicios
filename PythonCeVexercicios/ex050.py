# SOMA DE PARES #

import os

nome_programa = 'soma pares'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def quant_numeros():
    quantidade_numeros = int(input('Digite quantos números voce vai digitar: '))
    return quantidade_numeros

def recebendo_numeros(quantidade_numeros):
    soma = 0
    for i in range(1, quantidade_numeros + 1):
        numero = int(input('Digite o {}º número: '.format(i)))
        if numero % 2 == 0:
            soma += numero
    return soma

interface()
soma = recebendo_numeros(quant_numeros())
print('A soma dos números pares digitados é {}'.format(soma))