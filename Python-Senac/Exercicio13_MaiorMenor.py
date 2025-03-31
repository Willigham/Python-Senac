valor = 1
x = 1
maior = 0
menor = 999
while valor != 0:
    valor = int(input("Qual e o valor desse produto:"))
    if valor != 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    # x = int(input("0 para sair:"))
print(maior, menor)
    