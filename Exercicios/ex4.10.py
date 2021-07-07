"""
Calcular o preço a pagar pelo fornecimento de energia elétrica.
Perguntar a quantidade de kWh consumida e o tipo de instalção:
R para Residências
I para Indústrias
C para comércios
Calcular o preço a pagar de acordo com a tabela a seguir:
__________________________________________
TIPO        |    FAIXA (kWh)     | PREÇO
____________|____________________|________
Residencial | Até 500            | R$0,40
            | Acima de 500       | R$0,65
____________|____________________|________
Comercial   | Até 1000           | R$0,55
            | Acima de 1000      | R$0,60
____________|____________________|________
Industrial  | Até 5000           | R$0,55
            | Acima de 5000      | R$0,60
____________|____________________|________
"""
qtdkwh = float(input('Digite a quantidade de kWh consumida: '))
instalacao = input('Digite o tipo de instalação:\n'
                   'R para residências\n'
                   'C para comércios\n'
                   'I para indústrias\nQual sua instalação: ').upper()
if instalacao == 'R':
    if qtdkwh <= 500:
        print(f'Preço R${qtdkwh * 0.40:6.2f}    | RESIDENCIAL ATÉ 500')
    else:
        print(f'Preço R${qtdkwh * 0.65:6.2f}    | RESIDENCIAL ACIMA DE 500')

elif instalacao == 'C':
    if qtdkwh <= 1000:
        print(f'Preço R${qtdkwh * 0.55:6.2f}    | COMERCIAL ATÉ 1000')
    else:
        print(f'Preço R${qtdkwh * 0.60:6.2f}    | COMERCIAL ACIMA DE 1000')
elif instalacao == 'I':
    if qtdkwh <= 5000:
        print(f'Preço R${qtdkwh * 0.55:6.2f}    | INDUSTRIAL ATÉ 5000')
    else:
        print(f'Preço R${qtdkwh * 0.60:6.2f}    | INDUSTRIAL ACIMA DE 5000')
else:
    print('Você digitou algo diferente de R, C ou I. Tente novamente!')