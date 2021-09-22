"""
Abaixo de 200 minutos = R$0.20 por minuto
Entre 200 e 400 minutos = R$0.18 por minuto
Acima de 400 minutos = R$0.15 por minuto
"""
minutos = int(input('Quantos minutos você utilizou este mês: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f'Você vai pagar este mês: R${minutos * preco:6.2f}')