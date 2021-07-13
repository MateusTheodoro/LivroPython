questão = 1
pontos = 0

while questão <= 3:
    resposta = input(f"Digite a resposta da {questão}: ")

    if questão == 1 and (resposta == 'b' or resposta == 'B'):
        pontos = pontos + 1

    if questão == 2 and (resposta == 'a' or resposta == 'A'):
        pontos = pontos + 1

    if questão == 3 and (resposta == 'c' or resposta == 'C'):
        pontos = pontos + 1

    questão = questão + 1

print(f'O total de pontos é de: {pontos}')