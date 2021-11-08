"""
Contagem de cédulas
Execute o Programa para os seguintes valores: 501, 745, 384, 2, 7 e 1
"""
valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar = apagar - atual
        cedulas = cedulas + 1
    else:
        print(f"{cedulas} cédula(s) de R${atual}")
        if apagar == 0:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0