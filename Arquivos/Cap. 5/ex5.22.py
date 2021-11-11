"""
Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida.
Repita até que a opção de saída seja escolhida.
"""
while True:
    print("""
    Menu
    ---------
    1 - Adição 
    2 - Subtração 
    3 - Divisão 
    4 - Multiplicação
    5 - Sair
    """)

    opcao = int(input("Escolha uma opcao: "))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        n = int(input("Tabuada de: "))
        x = 1
        while x <= 10:
            if opcao == 1:
                print(f'{n} + {x} = {n + x}')
            elif opcao == 2:
                print(f'{n} - {x} = {n - x}')
            elif opcao == 3:
                print(f'{n} / {x} = {n / x:5.2f}')
            elif opcao == 4:
                print(f'{n} * {x} = {n * x}')
            x += 1
    else:
        print("Opção inválida")


# while True:
#     operacao = int(input("0 - Sair\n1 - adição\n2 - subtração\n3 - divisão\n4 - multiplicação\n"))
#     if operacao == 0:
#         break
#     if operacao == 1:
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f"{tabuada} + {numero} = {tabuada + numero}")
#                 numero += 1
#             tabuada += 1
#         print("\n")
#
#     if operacao == 2:
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f"{tabuada} - {numero} = {tabuada - numero}")
#                 numero += 1
#             tabuada += 1
#         print("\n")
#
#     if operacao == 3:
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f"{tabuada} / {numero} = {tabuada / numero}")
#                 numero += 1
#             tabuada += 1
#         print("\n")
#
#     if operacao == 4:
#         tabuada = 1
#         while tabuada <= 10:
#             numero = 1
#             while numero <= 10:
#                 print(f"{tabuada} * {numero} = {tabuada * numero}")
#                 numero += 1
#             tabuada += 1
#         print("\n")
#
#
