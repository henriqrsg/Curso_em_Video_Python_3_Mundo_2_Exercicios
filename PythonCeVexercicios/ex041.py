# CATEGORIA ATLETA #

import os

nome_programa = 'analisando categoria atleta'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

interface()
idade = int(input('Qual a idade do atleta: '))
if idade <= 9:
    print('A categoria do atleta é mirim!')
elif idade > 9 and idade <= 14:
    print('A categoria do atleta é infantil!')
elif idade > 14 and idade <= 19:
    print('A categoria do atleta é junior!')
elif idade > 19 and idade <= 20:
    print('A categoria do atleta é sênior!')
elif idade > 20:
    print('A categoria do atleta é master!')
elif idade < 0:
    print('Esta idade é inválida!')
