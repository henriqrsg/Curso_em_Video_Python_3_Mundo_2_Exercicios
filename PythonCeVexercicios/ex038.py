# COMPARANDO VALORES #

import os

nome_programa = 'comparando valores'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def pegando_numeros():
    lista_numeros = []
    quant_numeros = int(input('Digite a quantidade de números que deseja comparar: '))
    for i in range (quant_numeros):
        lista_numeros.append(int(input('Digite o {}º número que deseja fazer a comparação: '.format(i+1))))
    comparando(lista_numeros)

def comparando(lista_numeros):
    lista_numeros.sort()
    print('O maior valor da lista é o {} e o menor é o {}!'.format(lista_numeros[-1], lista_numeros[0]))


interface()
pegando_numeros()