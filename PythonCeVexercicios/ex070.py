# MERCADO LUIZ #

import os

nome_programa = 'mercado luiz'.upper()

def interface(carrinho):
    os.system('cls')
    print(70 * '=')
    print(f'{nome_programa:^70}')
    print(70 * '=')
    print('')
    print(f'Valor total: {carrinho}')
    print('')

def adicionando():
    produto_mais_caro = 0
    nome_produto_mais_caro = ''
    produto_mais_barato = 1000000
    nome_produto_mais_barato = ''
    quant_produtos_maisde1000 = 0
    carrinho = 0
    while True:
        interface(carrinho)
        nome = input('Nome do produto: ')
        preco = float(input('Valor do produto: R$ '))
        quantidade_produto = int(input(f'Digite quantos(as) {nome} você pegou: '))
        valor_produto = quantidade_produto * preco
        carrinho += valor_produto
        if preco > 1000:
            quant_produtos_maisde1000 +=1
        if preco > produto_mais_caro:
            produto_mais_caro = preco
            nome_produto_mais_caro = nome
        if preco < produto_mais_barato:
            produto_mais_barato = preco
            nome_produto_mais_barato = nome
        interface(carrinho)
        continuar = input('Deseja adicionar novos produtos ao carrinho ? [S/N]: ').upper()
        if continuar in ('NÃO', 'NAO', 'N'):
            break
            interface()
    print(f'O total da compra foi de R${carrinho:.2f}, com:\n{quant_produtos_maisde1000} produtos custando mais de 1000,\ne o produto mais caro foi o {nome_produto_mais_caro} custando R$ {produto_mais_caro:.2f},\ne o mais barato foi o {nome_produto_mais_barato} custando R$ {produto_mais_barato:.2f}')

adicionando()
