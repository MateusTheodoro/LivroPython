# x = 1
# while x <= 3:
#     x = x + 1
#     print(x)

# x = 10
# while x >= 0:
#     print(x)
#     x = x - 1
# print("Fogo!!")
#
# fim = int(input('Último número: '))
# x = 1
# while x <= fim:
#     print(x)
#     x += 1
#

# s = 0
# while True:
#     v = int(input("Digite um nro a somar ou 0 p/ sair: "))
#     if v == 0:
#         break
#     s += v
# print(s)

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
