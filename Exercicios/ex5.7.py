# Escolhendo como começar e terminar a tabuada

n = int(input('Tabuada de: '))
comeco = int(input('Digite o começo: '))
final = int(input('Digite o final: '))

x = comeco

while x <= final:
    print(f'{n}x{x} = {x * n}')
    x += 1
