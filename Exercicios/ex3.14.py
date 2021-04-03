km = int(input('Digite a quantidade em km: '))
dias = int(input('Digite a quantidade de dias: '))
preco = (60 * dias) + (km * 0.15)

print(f'O preço será de R${preco:.2f}')