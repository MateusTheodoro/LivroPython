notas = [6,7,5,8,9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:5.2f}")
