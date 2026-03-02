# MAIOR E MENOR PESO #

import os

nome_programa = 'verificador de pesos'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def extraindo_pesos():
    maior_peso = 0
    menor_peso = 1000000
    quant_pessoas = int(input('Digite a quantidade de pessos que você irá analisar os pesos: '))
    for i in range(1, quant_pessoas + 1):
        peso = float(input('Digite o peso da {}ª pessoa [kg]: '.format(i)))
        maior_peso, menor_peso = verificador(peso, maior_peso, menor_peso)
    return maior_peso, menor_peso

def verificador(peso, maior_peso, menor_peso):
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
    return maior_peso, menor_peso

interface()
maior_peso, menor_peso = extraindo_pesos()
print('O maior e o menor peso digitado foram de {:.1f}kg e {:.1f}kg respectivamente'.format(maior_peso, menor_peso))