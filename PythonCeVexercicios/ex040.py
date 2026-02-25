# MEDIA DE NOTAS #

import os

nome_programa = 'média de notas'.upper()

media_escola = 6

alunos = [
    {'nome': ' ', 'numero': ' ', 'nota1': ' ', 'nota2': ' ', 'media': ' '},
]

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')
    print()

def recebendo_notas(quant_alunos):
    for i in range(quant_alunos):
        nome = input('Digite o nome do {}º aluno: '.format(i+1)).upper()
        numero = i+1
        nota1 = float(input('Digite a 1ª nota de {}: '.format(nome)))
        nota2 = float(input('Digite a 2ª nota de {}: '.format(nome)))
        print()
        alunos.append({
                'nome': nome,
                'numero': numero,
                'nota1': nota1,
                'nota2': nota2,
                'media': (nota1 + nota2) / 2
             })

def aluno_escolhido():
    aluno_escolhido_nome = input('Digite qual o nome do aluno que deseja saber a média: ').upper()
    for aluno in alunos:
        if aluno['nome'] == aluno_escolhido_nome:
            media_aluno = aluno['media']
            print('A média de {} nas duas provas foi de {:.2f}!'.format(aluno_escolhido_nome, media_aluno))
            if media_aluno < media_escola:
                print('Como a média da escola é de {} e a média de {} foi de {:.2f} ele/a nao foi aprovado na matéria!'.format(media_escola, aluno_escolhido_nome, media_aluno))
            else: 
                    print('Parabéns! A média da escola é de {} e {} obteve a média de {:.2f}! Ele/a passou na matéria!'.format(media_escola, aluno_escolhido_nome, media_aluno))
            break
    else: 
        print('O aluno {} não existe!'.format(aluno_escolhido))
    continuar = input('Deseja ver a nota de outro aluno ? [S/N]: ').upper()
    if continuar in ('S', 'SIM'):
        interface()
        aluno_escolhido()

interface()
quant_alunos = int(input('Digite a quantidade de alunos que você quer ver a nota: '))
print()
recebendo_notas(quant_alunos)
interface()
aluno_escolhido()