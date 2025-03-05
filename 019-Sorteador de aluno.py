# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que o ajude,
# lendo os nomes e o escrevendo o nome escolhido

from random import choice
aluno_1 = str(input('Digite o nome do 1° aluno: ')).strip().title()
aluno_2 = str(input('Digite o nome de 2º aluno: ')).strip().title()
aluno_3 = str(input('Digite o nome do 3º aluno:')).strip().title()
aluno_4 = str(input('Digite o nome do 4º aluno: ')).strip().title()
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteado = choice(alunos)
print(f'O aluno sorteado para apagar o quadro foi: {sorteado}')
