def ParImpar(numero):
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")

num = int(input('Digite um número: '))

resultado = ParImpar(num)
print("O número", num, "é", resultado)
