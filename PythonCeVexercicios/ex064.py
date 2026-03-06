# LEITOR DE INTEIROS #

import os

nome_programa = 'leitor de inteiros'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def leitor():
    soma = -999
    numero = 0
    contador = -1
    while numero != 999:
        numero = int(input('Digite números inteiros a seguir,\nquando quiser parar digite [999]: '))
        interface()
        soma += numero
        contador += 1
    print('A soma dos {} numeros digitador é de {}'.format(contador, soma))

interface()
leitor()