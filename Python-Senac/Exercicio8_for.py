#programa que leia a idade de 5 pessoa
#soma das idades
#media
soma = 0
for i in range(5):
    idade = int(input("Informe a idade:"))
    soma = soma + idade

print("Soma das idades:", soma)
print("Media das idades:", soma / 5)