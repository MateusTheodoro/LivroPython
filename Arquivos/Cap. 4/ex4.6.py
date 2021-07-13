distancia = int(input('Digite a distância: '))

if distancia <= 200:
    print(f'O preço será de: R${distancia * 0.50:.2f}')
else:
    print(f'O preço será de: R${distancia * 0.45:.2f}')
