pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f'Resposta da questão {questao}: ')

    if questao == 1 and resposta == 'a':
        pontos = pontos + 1

    if questao == 2 and resposta == 'b':
        pontos = pontos + 1

    if questao == 3 and resposta == 'c':
        pontos = pontos + 1

    questao = questao + 1

print(f'Total de pontos: {pontos}')
