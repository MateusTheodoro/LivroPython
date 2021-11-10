"""
Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida.
Repita até que a opção de saída seja escolhida.
"""
while True:
    operacao = int(input("0 - Sair\n1 - adição\n2 - subtração\n3 - divisão\n4 - multiplicação\n"))
    if operacao == 0:
        break
    if operacao == 1:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
                numero += 1
            tabuada += 1
        print("\n")

    if operacao == 2:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} - {numero} = {tabuada - numero}")
                numero += 1
            tabuada += 1
        print("\n")

    if operacao == 3:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} / {numero} = {tabuada / numero}")
                numero += 1
            tabuada += 1
        print("\n")

    if operacao == 4:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} * {numero} = {tabuada * numero}")
                numero += 1
            tabuada += 1
        print("\n")


