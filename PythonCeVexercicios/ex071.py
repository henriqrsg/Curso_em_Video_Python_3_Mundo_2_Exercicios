#  #

import os

nome_programa = ''.upper()

def interface():
    os.system('cls')
    print(70 * '=')
    print(f'{nome_programa:^70}')
    print(70 * '=')
    print('')

interface()