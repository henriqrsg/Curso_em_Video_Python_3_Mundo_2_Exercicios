# SEQUÊNCIA DE FIBONACCI #

import os

nome_programa = 'sequência de fibonacci'.upper()

def interface():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa))
    print(70 * '=')
    print()

def fibonacci():
    quant_termos = int(input('Digite a quantidade de termos que você deseja ver da sequencia de fibonacci: '))
    c = 3
    t1 = 0
    t2 = 1
    print('O 1º termo da sequência é o 0')
    print('O 2º termo da sequência é o 1')
    while c <= quant_termos:
        termo = t1 + t2
        print('O {}º termo da sequência é o {}'.format(c, termo))
        t1 = t2
        t2 = termo
        c += 1

interface()
fibonacci()