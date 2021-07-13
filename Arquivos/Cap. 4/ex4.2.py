velocidade = int(input('Digite a velocidade do carro: '))
multa = velocidade * 5
if velocidade <= 80:
    print('Você está no limite, pode prosseguir!')
if velocidade > 80:
    print(f'Você está acima da velocidade, vai ser multado em R${multa:.2f}')