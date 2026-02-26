# JOKENPO #

import os

import random

nome_programa = 'jokenpo'.upper()

lista_jokenpo = [
    {'nome': 'pedra'},
    {'nome': 'papel'},
    {'nome': 'tesoura'},
]

def interface():
    os.system('cls')
    print(30 * '=')
    print('{:^30}'.format(nome_programa))
    print(30 * '=')
    print('')
    for i in range (len(lista_jokenpo)):
        print('[{}] {}'.format(i+1, lista_jokenpo[i]['nome']))
    print('')

def jogo():
    interface()
    numero_usuario = int(input('Escolha o número da sua jogada [1] [2] [3]: '))
    interface()
    numero_maquina = random.randint(1, len(lista_jokenpo))
    if numero_maquina == 1 and numero_usuario == 2 or numero_maquina == 2 and numero_usuario == 3 or numero_maquina == 3 and numero_usuario == 1:
        print('Eu escolhi o/a {}!'.format(lista_jokenpo[numero_maquina-1]['nome'].upper()))
        input('\033[1;32mDROGA VOCÊ VENCEU!\033[m')
    elif numero_maquina == numero_usuario:
        print('Eu escolhi o/a {}!'.format(lista_jokenpo[numero_maquina-1]['nome'].upper()))
        input('\033[1;36mEMPATAMOS!\033[m')
    else:
        print('Eu escolhi o/a {}!'.format(lista_jokenpo[numero_maquina-1]['nome'].upper()))
        input('\033[1;31mHAHA EU VENCI NESSA!\033[m')
    continuar()

def continuar():
    interface()
    resposta = input('Deseja continuar jogando ? [S/N]: ')
    if resposta.upper() in ('SIM, S'):
        jogo()
    else:
        print('Obrigado por jogar!')

interface()
jogo()