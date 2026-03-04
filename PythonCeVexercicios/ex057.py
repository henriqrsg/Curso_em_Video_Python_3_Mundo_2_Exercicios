# LEITOR DE GÊNERO #

import os

nome_programa = 'leitor de gênero'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def verificador_de_genero():
    genero = 's'
    while genero.upper() not in ('M, F'):
        genero = input('Digite o seu gênero [M/F]: ')
        if genero.upper() not in ('M, F'):
            input('Digite um gênero válido M ou F!')
            interface()
    interface()
    if genero.upper() == 'M':
        print('Olá pessoa do sexo Masculino!')
    else:
        print('Olá pessoa do sexo Feminino!')

interface()
verificador_de_genero()