# VERIFICADOR DE PALÍNDROMO #

import os

nome_programa = 'verificador de palíndromos'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def recebendo_palavra():
    palavra = input('Digite a palavra a ser verificada: ')
    return(palavra)

def verificador(palavra):
    palavra_sem_espaco = palavra.replace(' ','')
    if palavra_sem_espaco[len(palavra_sem_espaco)::-1].upper() == palavra_sem_espaco.upper():
        print('A palavra {} é um palíndromo! '.format(palavra))
    else:
        print('A palavra {} não é um palíndromo! '.format(palavra))

interface()
verificador(recebendo_palavra())