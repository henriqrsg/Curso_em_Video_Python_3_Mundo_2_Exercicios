# ANO NOVO #

import os
import time

nome_programa = 'contagem regressiva'.upper()

def interface():
    os.system('cls')
    print(30 * '=')
    print('{:^30}'.format(nome_programa))
    print(30 * '=')
    print('')

def contagem_regressiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)
    interface()
    print('🎆 🎉 👏 🥳')

interface()
contagem_regressiva()