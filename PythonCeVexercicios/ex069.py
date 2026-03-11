# ANALISADOR DE PESSOAS #

import os

nome_programa = 'analisador de pessoas'.upper()

pessoas = []

modo = 'n'

def interface(modo):
    os.system('cls')
    print(70 * '=')
    if modo == 'n':
        print(f'{nome_programa:^70}')
    else: 
        print(f'{'estatisticas'.upper():^70}')
    print(70 * '=')
    print('')

def analisar():
    quant_maiores_de_idade = 0
    quant_homem = 0
    quant_mulheres_mais_20 = 0
    
    while True:
        interface(modo)

        nome = input('Digite o nome da pessoa: ')
        idade = int(input('Digite a idade da pessoa: '))
        sexo = input('Digite o sexo da pessoa [M/F]: ')

        if idade > 18:
            quant_maiores_de_idade += 1
        if sexo.upper() == 'M':
            quant_homem += 1
        if sexo.upper() == 'F' and idade < 20:
            quant_mulheres_mais_20 += 1

        pessoa = {
            'nome': nome,
            'idade': idade,
            'sexo': sexo
        }

        pessoas.append(pessoa)

        print()
        continuar = input('Deseja continuar [S/N]: ')

        if continuar.upper() in ('NÃO', 'N', 'NAO'):
            break
    interface(modo = 'e')
    print(f'A) Foram cadastradas {quant_maiores_de_idade} pessoas maiores de 18 anos!')
    print(f'B) Foram cadastrados {quant_homem} homens!')
    print(f'C) Foram cadastradas {quant_mulheres_mais_20} mulheres com menos de 20 anos')

analisar()