"""
Para aprovar o empréstimo bancário: o valor da prestação mensal não pode ser superior a 30% do salário.
Perguntar: valor da casa, salário e a quantidade de anos a pagar.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
qtdAnos = int(input('Digite a quantidade de anos a pagar: '))
prestacao = casa / (qtdAnos * 12)
if prestacao > (30 / 100) * salario:
    print('O empréstimo foi negado! ')
else:
    print(f'Empréstimo aprovado. Valor das prestações são de: R${prestacao:6.2f}')
