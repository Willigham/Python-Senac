# Escreva um algoritmo que leia vários valores que representem o preço de produtos de uma loja, parar a leitura quando for informado o número 0. Após a leitura exibir:
# a. O valor médio dos produtos
# b. O valor do maior
# c. O valor do menor

x = 1
produto = 0
quantidade_produtos = 0
maior = 0
menor = 999

while x > 0:

    prduto = x + x
    quantidade_produtos = quantidade_produtos + 1
   
    if x > maior:
        maior = x

    if menor > x:
        menor = x
    print("-------------")
    x = int(input("[0] para Sair.\nValor do produto:"))
    #Digite "0" para "SAIR"
media = produto / quantidade_produtos
print("-----------------------------")
print("Valor médio dos produtos:", media)
print("O valor do maior:", maior)
print("O valor do menor:", menor)
