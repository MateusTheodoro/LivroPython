x = 1
soma = 0
while x <= 5:
    n = int(input(f'{x} Digite o número: '))
    soma += n
    x += 1
print(f'A média é: {soma / 5:5.2f}')