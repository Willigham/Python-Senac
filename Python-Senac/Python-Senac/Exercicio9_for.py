#programa que ler os valores e exibe a quantidade de numeros POSITIVOS e NEGATIVOS.

positivo = 0
negativo = 0

for i in range(10):
    valor = int(input("Informe o valor:"))
    if valor > 0:
        positivo = positivo + 1

    elif valor < 0:
        negativo = negativo + 1


print("Quantidade de números POSITIVOS::", positivo)
print("Quantidade de números NEGATIVOS:", negativo)

