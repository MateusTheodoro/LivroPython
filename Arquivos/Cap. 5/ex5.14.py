"""
Ler nros int;
Digitar zero p parar;
Final exibir: nros digitados, soma e média aritmética
"""

contador = 0
soma = 0
while True:
    nros = int(input("Digite os números e 0 para parar: "))

    if nros == 0:
        break

    contador += 1
    soma = soma + nros

print(f"Números digitados: {contador}\nSoma: {soma}\nMédia: {soma / contador}")