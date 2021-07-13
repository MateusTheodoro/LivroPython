n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
calculo = input('O que você deseja fazer? \n'
      'somar (+)\n'
      'subtrair (-)\n'
      'dividir (/)\n'
      'multiplicar (*)\n')

if calculo == '+':
    print(f'Você decidiu somar. O resultado é: {n1 + n2}')
elif calculo == '-':
    print(f'Você decidiu subtrair. O resultado é: {n1 - n2}')
elif calculo == '/':
    print(f'Você decidiu dividir. O resultado é: {n1 / n2}')
elif calculo == '*':
    print(f'Você decidiu multiplicar. O resultado é: {n1 * n2}')
else:
    print(f'Você escolheu {n1} e {n2} mas tivemos um problema. Reinicie o programa!')
