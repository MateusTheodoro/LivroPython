"""
Contagem de cédulas

Execute o Programa para os seguintes valores: 501, 745, 384, 2, 7 e 1

"""

valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1

    else:
        print(f"{cedulas} cédulas de R${atual}")
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        if atual == 20:
            atual = 10
        if atual == 10:
            atual = 5
        if atual == 5:
            atual = 1
        cedulas = 0
