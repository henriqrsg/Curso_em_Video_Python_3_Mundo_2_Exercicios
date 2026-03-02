# VERIFICADOR DE MAIORIDADE #

import os

nome_programa = 'verificador de maioridade'.upper()

lista_pessoas = []

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def extraindo_idades():
    quant_pessoas = int(input('Digite a quantidade de pessos que você irá analisar: '))
    for i in range(1, quant_pessoas + 1):
        lista_pessoas.append(int(input('Digite a idade da {}ª pessoa: '.format(i))))
    return quant_pessoas

def verificador(quant_pessoas):
    interface()
    for i in range(1, quant_pessoas + 1):
        if lista_pessoas[i-1] < 18:
            print('A pessoa de número {} não é maior de idade'.format(i))
        else:
            print('A pessoa de número {} é maior de idade'.format(i))

interface()
verificador(extraindo_idades())