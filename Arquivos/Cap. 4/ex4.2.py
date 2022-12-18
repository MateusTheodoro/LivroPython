"""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80 km/h
"""
velocidade = int(input('Qual a velocidade atual: '))

if velocidade > 80:
    velocidademulta = velocidade * 5
    print(f'Você está {velocidade - 80} km/h acima do permitido. Sua multa será de R${velocidademulta:.2f}')
elif velocidade == 80:
    print(f'Você está exatamente a 80 km/h e não pode correr mais. Cuidado!')
else:
    print(f'Você está na velocidade ideal. E pode acelerar mais {80 - velocidade} km/h.')