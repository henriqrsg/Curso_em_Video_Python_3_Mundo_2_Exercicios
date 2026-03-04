for c in range(1, 10):
    print(c)
print('Fim')


c = 1

while c < 10:
    print(c)
    c += 1
print('Fim')

continuar = True

while continuar == True:
    print('programa executando...')
    resposta = input('Deseja continuar ? [S/N]: ')
    if resposta.upper() in ('N, nao, não'):
        continuar = False