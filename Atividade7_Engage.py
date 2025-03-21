# Escreva um algoritmo que leia a idade de 6 pessoas, após a leitura exibir:
# a. A quantidade de pessoas menores de 18 anos
# b. A quantidade de pessoas maiores de 65 anos

#"a" será o valor iniciar do laço for e "b" será a quantidade de veres que ira repetir.
a = 0
b = 6

#valor inicial de pessoas menores e maiores de 18 anos.
menor = 0
maior = 0

#"range b" vai repetir a quantidade de veres da varial "b"
for a in range(b):
    idade = int(input("Informe a idade: "))
    if(idade < 18):
        menor = menor + 1
    else:
        maior = maior + 1

print("A quantidade de pessoas menores de 18 anos:", menor)
print("A quantidade de pessoas maiores de 18 anos:", maior)