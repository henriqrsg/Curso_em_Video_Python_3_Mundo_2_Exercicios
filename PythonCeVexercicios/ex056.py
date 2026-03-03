# ARMAZENADOR DE DADOS #

import os

lista_pessoas = []

estatistica = False

def interface(estatistica):
    if estatistica == True:
        nome_programa = 'análise das estatísticas'.upper()
    else: 
        nome_programa = 'armazenador de dados'.upper()
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa))
    print(70 * '=')
    print('')

def adicionando_pessoas_na_lista():
    quant_pessoas = int(input('Digite a quantidade de pessoas que você quer armazenar os dados: '))
    interface(estatistica)
    for i in range(quant_pessoas):
        print('--Dados da {}ª pessoa--'.format(i+1))
        print('')
        lista_pessoas.append({
        'nome': input('Nome da {}ª pessoa: '.format(i+1)).upper(),
        'idade': int(input('Idade da {}ª pessoa: '.format(i+1))),
        'sexo': input('Sexo da {}ª pessoa [M/F]: '.format(i+1)).upper()})
        interface(estatistica)
    
    return quant_pessoas

def media_idade(quant_pessoas):
    media = sum(pessoa['idade'] for pessoa in lista_pessoas) / quant_pessoas
    print('A média de idade das pessoas digitadas é de {:.2f} anos'.format(media))

def homem_mais_velho():
    maior_idade = 0
    homem_mais_velho = None
    for pessoa in lista_pessoas:
        if pessoa['sexo'] == 'M':
            if pessoa['idade'] > maior_idade:
                maior_idade = pessoa['idade']
                homem_mais_velho = pessoa['nome']
    print('O homem mais velho dos que foram digitados é o {} com {} anos'.format(homem_mais_velho, maior_idade))

def quant_mulheres_maiores_de_idade():
    quant_mulheres_maioridade = 0
    for pessoa in lista_pessoas:
        if pessoa['sexo'] == 'F' and pessoa['idade'] >= 18:
            quant_mulheres_maioridade += 1
    print('Existem {} mulheres na lista que são maiores de idade! '.format(quant_mulheres_maioridade))

def estatisticas(quant_pessoas):
    estatistica = True
    interface(estatistica)
    media_idade(quant_pessoas)
    homem_mais_velho()
    quant_mulheres_maiores_de_idade()

interface(estatistica)
estatisticas(adicionando_pessoas_na_lista())