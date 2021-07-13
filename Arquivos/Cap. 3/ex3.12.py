distancia = float(input('Digite a distância: '))
velocidade = float(input('Digite a velocidade média (km/h): '))
tempo = (distancia / velocidade) * 60
print(f'A distância será de {tempo:.2f} MINUTOS')
