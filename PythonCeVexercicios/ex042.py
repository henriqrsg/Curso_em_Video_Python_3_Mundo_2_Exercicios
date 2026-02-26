# VERIFICAÇÃO DE EXISTÊNCIA DE TRIÂNGULOS #

import os

nome_programa = 'verificando existencia do triângulo'.upper()

lados_triangulo = []

def interface():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa))
    print(70 * '=')
    print('')

def pegando_lados():
    for i in range(3):
        lados_triangulo.append(int(input('Digite quanto mede o {}º lado do triângulo: '.format(i+1))))

def condicao_existencia_triangulo():
    if lados_triangulo[0] > lados_triangulo[1] + lados_triangulo[2] or lados_triangulo[1] > lados_triangulo[0] + lados_triangulo[2] or lados_triangulo[2] > lados_triangulo[0] + lados_triangulo[1]:
        print('Estes valores de lados não podem formar um triângulo! ')
    else:
        classificacao_triangulo()

def classificacao_triangulo():
    if lados_triangulo[0] == lados_triangulo[1] and lados_triangulo[0] == lados_triangulo[2]:
        print('Este triângulo é equilátero!')
    elif lados_triangulo[0] != lados_triangulo[1] and lados_triangulo[0] != lados_triangulo[2] and lados_triangulo[1] != lados_triangulo[2]:
        print('Este triângulo é escaleno!')
    else:
        print('Este triângulo é isósceles!')

interface()
pegando_lados()
condicao_existencia_triangulo()