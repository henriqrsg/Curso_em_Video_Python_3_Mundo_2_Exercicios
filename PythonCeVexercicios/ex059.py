# MINICALCULADORA #

import os

nome_programa = 'mini-calculadora'.upper()

lista_funcionalidades = [
    {'nome': 'somar'},
    {'nome': 'multiplicar'},
    {'nome': 'maior'},
    {'nome': 'sair do programa'}
]

lista_numeros = []

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()
    for i in range(len(lista_funcionalidades)):
        print('[{}] {}'.format(i+1, lista_funcionalidades[i]['nome'].upper()))
    print()

def programa():
    interface()
    resposta = 0
    while resposta != 4:
        lista_numeros.clear()
        resposta = int(input('Digite o número do que deseja fazer: '))
        interface()
        if resposta == 1:
            continuar = 'S'
            while continuar.upper() not in('N, NÃO, NAO'):
                lista_numeros.append(int(input('Digite o número que deseja somar: ')))
                continuar = input('Deseja somar outro número? [S/N]: ')
            soma = sum(lista_numeros)
            interface()
            input('A soma dos números digitados é: {}'.format(soma))
            interface()
        elif resposta == 2:
            continuar = 'S'
            multiplicacao = 1
            while continuar.upper() not in('N, NÃO, NAO'):
                numero = int(input('Digite o número que deseja multiplicar: '))
                continuar = input('Deseja multiplicar outro número? [S/N]: ')
                multiplicacao *= numero
            interface()
            input('A multiplicação dos números digitados é: {}'.format(multiplicacao))
            interface()
        elif resposta == 3:
            numero_maior = 0
            quant_numeros = int(input('Digite a quantidade de números que você irá inserir para a verificação: '))
            interface()
            for i in range(quant_numeros):
                numero = int(input('Digite os números que deseja verificar qual o maior: '))
                if numero > numero_maior:
                    numero_maior = numero
            interface()
            input('O maior número digitado foi o {}'.format(numero_maior))
            interface()
        elif resposta == 4:
            print('Obrigado por utilizar o programa!')
        else:
            input('Digite o número de uma funcionalidade válida! ')
            programa()

programa()