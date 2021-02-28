dia = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

totalSegundos = (dia * 86400) + (horas * 3600) + (minutos * 60) + segundos

print (f'A quantidade de {dia} dias, {horas} horas, {minutos} minutos e {segundos} segundos correspondem a {totalSegundos} segundos')