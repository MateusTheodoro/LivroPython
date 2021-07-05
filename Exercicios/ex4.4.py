salario = float(input('Digite o salário: '))

if salario >= 1251:
    aumentodez = salario * (10 / 100) + salario
    print(f'R${aumentodez:.2f}')

if salario <= 1250:
    aumentoquinze = salario * (15 / 100) + salario
    print(f'R${aumentoquinze:.2f}')

