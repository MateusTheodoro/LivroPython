"""
Escreva um programa que leia um número e verifique se é ou não um número primo.
Para fazer essa verificação, calcule o resto da divisão do número
por 2 e depois por todos os números ímpares até o número lido.
Se o resto de uma dessas divisões for igual a zero, o número não é primo.
Observe que 0 e 1 não são primos e que 2 é o único número que é par.
"""
nro = int(input("Digite um número: "))
if nro < 0:
    print("Número inválido. Digite apenas valores positivos")
if nro == 0 or nro == 1:
    print(f"{nro} é um caso especial.")
else:
    if nro == 2:
        print("2 é primo")
    elif nro % 2 == 0:
        print(f"{nro} não é primo, pois 2 é o único número par primo")
    else:
        x = 3
        while(x < nro):
            if nro % x == 0:
                break
            x += 2
        if x == nro:
            print(f"{nro} é primo")
        else:
            print(f"{nro} não é primo, pois é divisível por {x}")
