# CAIXA ELETRÔNICO #

import os

nome_programa = 'caixa eletrônico'.upper()

saldo = 432.00

senha_correta = 'abc123'

usuario_correto = 'teste'

def interface_inicial():
    os.system('cls')
    print(70 * '=')
    print(f'{nome_programa:^70}')
    print(70 * '=')
    print('')

def funcionalidade():
    while True:
        interface_inicial()
        print('[1] DEPÓSITO')
        print('[2] SAQUE')
        print()
        fazer = int(input('O que deseja fazer [1] [2]: '))
        if fazer == 1:
            deposito()
        elif fazer == 2:
            saque()
        else:
            print()
            input('Esta funcionalidade não existe, favor digite uma funcionalidade existente!')

def interface_deposito():
    os.system('cls')
    print(70 * '=')
    print(f'{'DEPÓSITO':^70}')
    print(70 * '=')
    print('')

def interface_saque():
    os.system('cls')
    print(70 * '=')
    print(f'{'SAQUE':^70}')
    print(70 * '=')
    print('')
    
def deposito():
    tentativas = 0
    global saldo
    while True:
        interface_deposito()
        usuario = input('Digite o seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        print()
        if usuario != usuario_correto or senha != senha_correta:
            input('Usuário ou senha incorretos!')
            tentativas += 1
            if tentativas == 3:
                interface_deposito()
                input('Número de tentativas excedido! Tente mais novamente mais tarde!')
                print()
                break
        else:
            while True:
                interface_deposito()
                print(f'Ola senhor {usuario_correto}'.upper().center(70))
                print('')
                print(f'Saldo: R$ {saldo:.2f}')
                print('')
                valor_deposito = float(input('Deseja fazer o depósito de quantos reais ? R$ '))
                if valor_deposito < 0:
                    print()
                    input('Por favor digite um número positivo!')
                elif valor_deposito == 0:
                    print()
                    input('Não faz sentido fazer um depósito de R$ 0.00')
                else:
                    saldo += valor_deposito
                    interface_deposito()
                    print(f'Ola senhor {usuario_correto}'.upper().center(70))
                    print('')
                    print(f'Saldo: R$ {saldo:.2f}')
                    print('')
                    continuar = input('Deseja fazer outro depósito ? [S/N]: ').upper()
                    if continuar in ('NÃO', 'NAO', 'N'):
                        interface_deposito()
                        print(f'O novo saldo de sua conta é de: R$ {saldo:.2f}')
                        print('')
                        input('Obrigado por utilizar nosso caixa eletrônico!')
                        print('')
                        break
            break

def saque():
    tentativas = 0
    global saldo
    while True:
        interface_saque()
        usuario = input('Digite o seu nome de usuário: ')
        senha = input('Digite sua senha: ')
        print()
        if usuario != usuario_correto or senha != senha_correta:
            input('Usuário ou senha incorretos!')
            tentativas += 1
            if tentativas == 3:
                interface_saque()
                input('Número de tentativas excedido! Tente mais novamente mais tarde!')
                print()
                break
        else:
            while True:
                interface_saque()
                print(f'Ola senhor {usuario_correto}'.upper().center(70))
                print('')
                print(f'Saldo: R$ {saldo:.2f}')
                print('')
                valor_saque = float(input('Deseja fazer um saque de quantos reais ? R$ '))
                if valor_saque < 0:
                    print()
                    input('Por favor digite um número positivo!')
                elif valor_saque == 0:
                    print()
                    input('Não faz sentido fazer um saque de R$ 0.00')
                else:
                    if valor_saque > saldo:
                        print('')
                        input('Você não tem saldo suficiente para o saque!')
                    else:
                        saldo -= valor_saque
                        interface_saque()
                        print(f'Ola senhor {usuario_correto}'.upper().center(70))
                        print('')
                        print(f'Saldo: R$ {saldo:.2f}')
                        print('')
                        continuar = input('Deseja fazer outro saque ? [S/N]: ').upper()
                        if continuar in ('NÃO', 'NAO', 'N'):
                            interface_saque()
                            print(f'O novo saldo de sua conta é de: R$ {saldo:.2f}')
                            print('')
                            input('Obrigado por utilizar nosso caixa eletrônico!')
                            print('')
                            break
            break

funcionalidade()