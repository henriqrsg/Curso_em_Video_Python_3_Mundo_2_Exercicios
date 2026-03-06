# ESTATÍSTICA #

import os

nome_programa = 'estatística'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def leitor_dados():
    dados = 0
    maior = 0
    menor = 1000000
    soma = 0
    media = 0
    c = 0
    resposta = 'sim'
    while resposta.upper() not in ('NÃO, N, NAO'):
        dados = int(input('Digites os dados a seguir: '))
        soma += dados
        c += 1
        media = soma / c
        if dados > maior:
            maior = dados
        if dados < menor:
            menor = dados
        resposta = input('Deseja continuar [S/N]: ')
        interface()
    print('A média dos dados digitados foi de: {:.1f},\no maior valor digitado foi o: {},\ne o menor valor digitado foi o: {}'.format(media, maior, menor))

interface()
leitor_dados()