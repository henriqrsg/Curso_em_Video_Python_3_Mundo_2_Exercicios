# IMC #

import os

nome_programa = 'categoria do seu imc'.upper()

lados_triangulo = []

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print('')

def extraindo_valores():
    altura = float(input('Digite quantos metros você tem [ex: 1.73m]: '))
    print('')
    peso = float(input('Digite quanto você pesa [ex: 80.3kg]:'))
    print('')
    calculo_imc(altura, peso)

def calculo_imc(altura, peso):
    imc = peso / (altura ** 2)
    classificacao_imc(imc)

def classificacao_imc(imc):
    if imc < 18.5:
        print('Você esta abaixo do peso!')
    elif imc >= 18.5 and imc < 25:
        print('Você está no peso ideal!')
    elif imc >= 25 and imc < 30:
        print('Você esta com sobrepeso!')
    elif imc >= 30 and imc < 40:
        print('Você esta com obesidade')
    elif imc > 40:
        print('Você esta com obesidade mórbida')

interface()
extraindo_valores()
