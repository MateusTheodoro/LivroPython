"""
Imprimir até o último número digitado pelo usuário mostrando apenas os números ímpares.
"""

nro = int(input('Digite o último número a imprimir: '))
x = 0
while x <= nro:
    if x % 2 != 0:
        print(x)
    x += 1
