"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
"""
# depósito = float(input("Depósito inicial: "))
# taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
# mês = 1
# saldo = depósito
# while mês <= 24:
#     saldo = saldo + (saldo * (taxa / 100))
#     print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
#     mês = mês + 1
# print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")

deposito = float(input('Digite o depósito: '))
taxa = float(input('Digite a taxa de juros: '))

mês = 1
saldo = deposito

while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f'Mês {mês}: R${saldo:5.2f}')
    mês += 1
print(f'O juros será de R${saldo-deposito:8.2f}')
