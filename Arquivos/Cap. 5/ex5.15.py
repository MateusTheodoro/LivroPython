preco = 0
contador = 0
while True:
    codigo = int(input('Digite o código: '))

    if codigo == 0:
        break

    elif codigo == 1:
        preco = preco + 0.50

    elif codigo == 2:
        preco += 1

    elif codigo == 4:
        preco += 4

    elif codigo == 5:
        preco += 7

    elif codigo == 9:
        preco += 8

    else:
        print("Código inválido")
        contador -= 1

    contador += 1


print(f'Total de compras: {contador}\t Total preço: R$: {preco:.2f}')



