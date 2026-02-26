# PAGAMENTO EM LOJA #

import os

nome_programa = 'desconto com pagamento'.upper()

lista_produtos = [
    {'nome': 'Arroz 5kg', 'preco': 24.90},
    {'nome': 'Feijão 1kg', 'preco': 8.50},
    {'nome': 'Macarrão 500g', 'preco': 4.75},
    {'nome': 'Óleo de Soja 900ml', 'preco': 6.99},
    {'nome': 'Leite 1L', 'preco': 4.39},
    {'nome': 'Açúcar 1kg', 'preco': 3.89},
    {'nome': 'Café 500g', 'preco': 15.90},
    {'nome': 'Manteiga 200g', 'preco': 9.49},
    {'nome': 'Refrigerante 2L', 'preco': 7.99},
    {'nome': 'Sabão em Pó 1kg', 'preco': 12.50}
]

lista_metodos_pagamento = [
    {'nome': 'Dinheiro', 'desconto': 0.10},
    {'nome': 'PIX', 'desconto': 0.15},
    {'nome': 'Cartão de Débito', 'desconto': 0.1},
    {'nome': 'Cartão de Crédito', 'desconto': 0.0},
    {'nome': 'Vale Alimentação', 'desconto': 0.05},
    {'nome': 'Boleto Bancário', 'desconto': 0.0}
]

carrinho = 0

def interface(carrinho):
    os.system('cls')
    print(60 * '=')
    print('{:^60}'.format(nome_programa))
    print(60 * '=')
    print('')
    for i in range(len(lista_produtos)):
        print(' [{}] {}'.format(i+1, lista_produtos[i]['nome']))
    print('')
    print('TOTAL DA COMPRA {:.2f}'.format(carrinho))
    print('')

def mostrando_produtos(carrinho):
    interface(carrinho)
    escolhendo_produto(carrinho)

def escolhendo_produto(carrinho):
    numero_produto = int(input('Digite qual o número do produto que deseja comprar: '))
    if numero_produto not in range(1, len(lista_produtos) + 1):
        print('Desculpe mas não temos este produto no estoque! ')
        continuar_compra(carrinho)
    else:
        interface(carrinho)
        nome_produto = lista_produtos[numero_produto - 1]['nome']
        preco_produto = lista_produtos[numero_produto - 1]['preco']
        quant_produto = int(input('O produto {} esta custando R${:.2f}, quantas unidades você deseja levar: '.format(nome_produto, preco_produto)))
        interface(carrinho)
        valor_produto = quant_produto * preco_produto
        resposta = input('{} unidades do produto {} custam R${}! Deseja adicionar {} unidades do produto {} no carrinho ? [S/N]: '.format(quant_produto, nome_produto, valor_produto, quant_produto, nome_produto)).upper()
        if resposta in ('S', 'SIM'):
            carrinho = valor_produto + carrinho
        interface(carrinho)
        continuar_compra(carrinho)

def continuar_compra(carrinho):
    continuar_comprando = input('Deseja comprar outro item? [S/N]: ').upper()
    if continuar_comprando in ('S', 'SIM'):
        mostrando_produtos(carrinho)
    else:
        pagamento(carrinho)

def interface_compra(carrinho):
    os.system('cls')
    print(60 * '=')
    print('{:^60}'.format('pagamento'.upper()))
    print(60 * '=')
    print('')
    for i in range(len(lista_metodos_pagamento)):
        print(' [{}] {}'.format(i+1, lista_metodos_pagamento[i]['nome']))
    print('')
    print('TOTAL DA COMPRA {:.2f}'.format(carrinho))
    print('')

def pagamento(carrinho):
    if carrinho != 0:
        interface_compra(carrinho)
        numero_pagamento = int(input('Digite o número do método de pagamento que irá utilizar: '))
        interface_compra(carrinho)
        if numero_pagamento not in range(1, len(lista_metodos_pagamento) + 1):
            input('Desculpe, esta forma de pagamento não existe! Digite ENTER para tentar novamente! ')
            pagamento(carrinho)
        else: 
            nome_pagamento = lista_metodos_pagamento[numero_pagamento - 1]['nome']
            desconto_pagamento = lista_metodos_pagamento[numero_pagamento - 1]['desconto']
            valor_descontado = carrinho - (desconto_pagamento * carrinho)
            print('O método de pagamento {} tem desconto de {:.2f}%'.format(nome_pagamento, desconto_pagamento * 100))
            input('Assim sua compra no valor de R${} com o desconto de {:.2f}% irá passar a custar R${:.2f}, digite ENTER para finalizar'.format(carrinho, desconto_pagamento * 100, valor_descontado))
    interface_compra(carrinho)
    print('Muito obrigado por comprar em nosso estabelecimento!')

mostrando_produtos(carrinho)