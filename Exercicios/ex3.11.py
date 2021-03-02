produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o desconto: '))
total = produto - (produto * (desconto / 100))

print(f'Com o desconto de {desconto:.0f}% o preço do produto será de: R${total:.2f}')
