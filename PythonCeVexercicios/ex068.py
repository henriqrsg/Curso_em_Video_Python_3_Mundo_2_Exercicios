# PAR OU ÍMPAR #

import os

import random

nome_programa = 'par ou ímpar'.upper()

def interface():
    os.system('cls')
    print(70 * '=')
    print(f'{nome_programa:^70}')
    print(70 * '=')
    print('')

def par_impar():
    vitorias = 0
    while True:
        interface()
        print()
        escolha = input('Vamos jogar PAR ou ÍMPAR! Escolha se quer ser PAR OU ÍMPAR [P/I]: ')
        print('')
        numero_pc = random.randint(0,10)
        numero_usuario = int(input('Digite um número: '))
        print()
        if escolha.upper() in ('I', 'ÍMPAR', 'IMPAR'):
            if (numero_pc + numero_usuario) % 2 == 1:
                input(f'\033[1;32mDroga você ganhou! Eu escolhi {numero_pc} e você {numero_usuario}, portanto deu ÍMPAR!\033[m')
                vitorias += 1
            else: 
                input(f'\033[1;31mHaha eu ganhei! Eu escolhi {numero_pc} e você {numero_usuario}, portanto deu PAR!\033[m')
                break
        else:
            if (numero_pc + numero_usuario) % 2 == 1:
                input(f'\033[1;31mHaha eu ganhei! Eu escolhi {numero_pc} e você {numero_usuario}, portanto deu ÍMPAR!\033[m')
                break
            else:
                input(f'\033[1;32mDroga você ganhou! Eu escolhi {numero_pc} e você {numero_usuario}, portanto deu PAR!\033[m')
                vitorias += 1
    print()
    print(f'\033[1;36mO jogo acabou porque você perdeu! Você conseguiu {vitorias} consecutivas!\033[m')

par_impar()
