# TESTE SUA SORTE #

import os

import random

nome_programa = 'teste sua sorte'.upper()

def interface():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa))
    print(70 * '=')
    print()

def teste_sua_sorte():
    quant = int(input('Você quer que eu escolha um número entre 0 e quanto: '))
    numero_compt = random.randint(0, quant)
    tentativas = 1
    numero_pessoa = int(input('Estou pensando em número entre 0 e {}, qual você acha que é: '.format(quant)))
    while numero_pessoa != numero_compt:
        interface()
        numero_pessoa = int(input('Você errou! Tente novamente: '))
        tentativas += 1
    interface()
    if tentativas == 1:
        print('Parabéns! Você acertou de primeira!')
    else:
        print('Parabéns! Você acertou em {} tentativas! '.format(tentativas))

interface()
teste_sua_sorte()