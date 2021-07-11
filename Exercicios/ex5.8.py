"""
Escreva um programa que leia dois números.
Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
Assim, 4x5 = 5+5+5+5 = 4+4+4+4+4
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

x = 1
while x <= n2:
    print(x)
    x = x + 1



#
# x = 1
# while x <= 10:
#     y = 1
#     while y <= 5:
#         print(f'{x}, {y}')
#         y += 1
#     x += 1
# print('Acabou!')