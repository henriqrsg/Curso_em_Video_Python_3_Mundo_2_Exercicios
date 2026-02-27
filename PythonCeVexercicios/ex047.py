# MOSTRANDO PARES #

import os

nome_programa = 'mostrando pares'.upper()

def interface():
    os.system('cls')
    print(30 * '=')
    print('{:^30}'.format(nome_programa))
    print(30 * '=')
    print('')

def mostrandopares():
    for p in range(2, 52, 2):
        print(p)

interface()
mostrandopares()