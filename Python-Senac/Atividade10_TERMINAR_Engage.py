# Escreva um algoritmo que leia vários valores que representem o preço de produtos de uma loja, parar a leitura quando for informado o número 0. Após a leitura exibir:
# a. O valor médio dos produtos
# b. O valor do maior
# c. O valor do menor

valor = 1
soma = 0
quant = 0
maior = 0
menor = 999

while valor != 0:

    valor = int(input("Valor do produto:"))
    soma = soma + valor
    quant = quant + 1
    if valor != 0:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor
    
media = soma / quant
print("Valor médio dos produtos:", media)
print("O valor do maior:", maior)
print("O valor do menor:", menor)
