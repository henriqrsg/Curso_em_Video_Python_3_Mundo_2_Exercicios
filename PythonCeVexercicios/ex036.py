# APROVAÇÃO DE EMPRÉSTIMO #

import os

nome_programa = 'aprovação de empréstimo bancário'.upper()

imoveis = [
    {'nome': 'casa', 'numero_imovel': 1},
    {'nome': 'apartamento', 'numero_imovel': 2},
    {'nome': 'fazenda', 'numero_imovel': 3},
]

def interface():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa))
    print(70 * '=')
    print('')

def interface_analise():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format('VAMOS ANALISAR SUAS CONDIÇÕES'))
    print(70 * '=')
    print('')

def escolha_do_imovel():
    for n in range(len(imoveis)):
        print('[{}] {}'.format(n+1, imoveis[n]['nome'].upper()))
    print('')
    numero_imovel = int(input('Digite o número do imóvel que deseja comprar com o empréstimo [1] [2] [3]: '))
    if numero_imovel not in range(1, len(imoveis)+1):
        input(print('Digite um número de imóvel correto'))
        interface()
        escolha_do_imovel()
    print('')
    valor_imovel = int(input('Qual o valor do/a {}: R$ '.format(imoveis[numero_imovel-1]['nome'].upper())))
    return valor_imovel

def condicao_emprestimo(prestacao_mensal, salario_cliente):
    if prestacao_mensal > 0.3 * salario_cliente:
        print('Por nossas políticas do Banco, o empréstimo do/a Senhor/a foi negado! ')
    else:
        print('Parabéns o seu empréstimo para compra do imóvel foi aprovado! ')

def analise(valor_imovel):
    salario_cliente = float(input('Digite qual seu salário médio mensal: '))
    quant_parcelas = 12 * int(input('Em quantos anos o senhor deseja pagar: '))
    prestacao_mensal = valor_imovel / quant_parcelas
    condicao_emprestimo(prestacao_mensal, salario_cliente)

interface()
valor_imovel = escolha_do_imovel()
interface_analise()
analise(valor_imovel)

print(valor_imovel)