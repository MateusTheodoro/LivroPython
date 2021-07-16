"""
Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
"""
#
# deposito = float(input('Depósito de: '))
# taxa = float(input('Taxa de: '))
# mensal = float(input('Depósito mensal de: '))
#
# mês = 1
# saldo = deposito
#
# while mês <= 24:
#     saldo = saldo + (saldo * (taxa / 100)) + mensal
#     print(f'Mês {mês}: R$ {saldo:5.2f}')
#     mês += 1
# print(f'O juros será de: R$ {saldo-deposito:8.2f}')


depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal: "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")