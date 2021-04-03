cigarros = int(input('Digite a quantide de cigarros por dia: '))
anos = int(input('Quantos anos você fumou? '))

diasquefuma = anos * 365
minutos = cigarros * 10
minutosperdidos = diasquefuma * minutos

print(f'--- Considerando que você perde 10 minutos da vida fumando ---')
print(f'Você perdeu {minutosperdidos} minutos, que corresponde a {minutosperdidos / 1440:.2f} dias da sua vida fumando')