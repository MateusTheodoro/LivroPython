salario = float(input('Digite o salário: '))
aumento = float(input('Digite o aumento (sem a %): '))
salarioTotal = salario + (salario * (aumento / 100))

print(f'O novo salário com o aumento de {aumento:.0f}% será de: R${salarioTotal:.2f}')
